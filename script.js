/* PetShop Amigo Fiel - scripts do site */

const HORA_ABERTURA = 8;
const HORA_FECHAMENTO = 17;

const SERVICOS = {
  banho: { nome: "Banho", preco: "R$ 50,00" },
  tosa: { nome: "Tosa", preco: "R$ 60,00" },
  banhoTosa: { nome: "Banho + Tosa", preco: "R$ 95,00" },
};

const METODOS = {
  telebusca: "Tele-busca",
  entregaLocal: "Entrega no local",
};

const PROMOCOES = [
  "🐾 Banho + Tosa por R$ 95,00: economize R$ 15,00 no pacote completo!",
  "🚚 Tele-busca disponível: buscamos seu pet em casa no horário agendado.",
  "📅 Atendemos de segunda a sábado, das 8h às 17h.",
];

/* ---------- Utilitários ---------- */

function apenasDigitos(valor) {
  return valor.replace(/\D/g, "");
}

function estaAberto(data = new Date()) {
  const dia = data.getDay(); // 0 = domingo
  const hora = data.getHours();
  return dia !== 0 && hora >= HORA_ABERTURA && hora < HORA_FECHAMENTO;
}

function formatarDataISO(iso) {
  const [ano, mes, dia] = iso.split("-");
  return `${dia}/${mes}/${ano}`;
}

function hojeISO() {
  const d = new Date();
  const mes = String(d.getMonth() + 1).padStart(2, "0");
  const dia = String(d.getDate()).padStart(2, "0");
  return `${d.getFullYear()}-${mes}-${dia}`;
}

/* ---------- Rodapé, relógio e status ---------- */

function atualizarAno() {
  document.querySelectorAll("#ano-atual").forEach((el) => {
    el.textContent = new Date().getFullYear();
  });
}

function atualizarRelogios() {
  const agora = new Date();
  const texto = agora.toLocaleString("pt-BR", {
    weekday: "long",
    day: "2-digit",
    month: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });

  ["relogio", "relogio-agenda"].forEach((id) => {
    const el = document.getElementById(id);
    if (el) el.textContent = texto;
  });

  const aberto = estaAberto(agora);
  const mensagem = aberto ? "Aberto agora" : "Fechado agora";

  ["status-funcionamento", "status-contato", "status-agenda"].forEach((id) => {
    const el = document.getElementById(id);
    if (!el) return;
    el.textContent = mensagem;
    el.classList.add("badge");
    el.classList.toggle("bg-success", aberto);
    el.classList.toggle("bg-secondary", !aberto);
  });
}

function iniciarPromocoes() {
  const el = document.getElementById("msg-promo");
  if (!el) return;
  let indice = 0;
  el.textContent = PROMOCOES[indice];
  setInterval(() => {
    indice = (indice + 1) % PROMOCOES.length;
    el.textContent = PROMOCOES[indice];
  }, 5000);
}

function iniciarNavbar() {
  const navbar = document.getElementById("navbar-principal");
  if (!navbar) return;
  const atualizar = () => {
    navbar.style.boxShadow = window.scrollY > 10 ? "0 4px 18px rgba(0,0,0,0.12)" : "";
  };
  window.addEventListener("scroll", atualizar);
  atualizar();
}

/* ---------- Máscaras ---------- */

function mascaraCPF(valor) {
  const d = apenasDigitos(valor).slice(0, 11);
  return d
    .replace(/(\d{3})(\d)/, "$1.$2")
    .replace(/(\d{3})(\d)/, "$1.$2")
    .replace(/(\d{3})(\d{1,2})$/, "$1-$2");
}

function mascaraTelefone(valor) {
  const d = apenasDigitos(valor).slice(0, 11);
  if (d.length <= 2) return d.length ? `(${d}` : "";
  if (d.length <= 3) return `(${d.slice(0, 2)}) ${d.slice(2)}`;
  if (d.length <= 7) return `(${d.slice(0, 2)}) ${d.slice(2, 3)} ${d.slice(3)}`;
  return `(${d.slice(0, 2)}) ${d.slice(2, 3)} ${d.slice(3, 7)}-${d.slice(7)}`;
}

function mascaraCEP(valor) {
  const d = apenasDigitos(valor).slice(0, 8);
  return d.length > 5 ? `${d.slice(0, 5)}-${d.slice(5)}` : d;
}

function aplicarMascara(id, mascara) {
  const campo = document.getElementById(id);
  if (!campo) return;
  campo.addEventListener("input", () => {
    campo.value = mascara(campo.value);
  });
}

/* ---------- Validações ---------- */

function cpfValido(cpf) {
  const d = apenasDigitos(cpf);
  if (d.length !== 11 || /^(\d)\1{10}$/.test(d)) return false;

  for (let t = 9; t < 11; t++) {
    let soma = 0;
    for (let i = 0; i < t; i++) soma += Number(d[i]) * (t + 1 - i);
    const digito = ((soma * 10) % 11) % 10;
    if (digito !== Number(d[t])) return false;
  }
  return true;
}

function marcarCampo(campo, valido) {
  campo.classList.toggle("is-invalid", !valido);
  campo.classList.toggle("is-valid", valido);
}

function validarCamposObrigatorios(form) {
  let tudoValido = true;
  form.querySelectorAll("input, select, textarea").forEach((campo) => {
    if (campo.type === "radio" || campo.type === "hidden") return;
    if (!campo.willValidate) return;
    const valido = campo.checkValidity();
    if (campo.required || campo.value) marcarCampo(campo, valido);
    if (!valido) tudoValido = false;
  });
  return tudoValido;
}

function grupoRadioValido(form, nome) {
  return form.querySelector(`input[name="${nome}"]:checked`) !== null;
}

/* ---------- Formulário de cadastro ---------- */

function iniciarCadastro() {
  const form = document.getElementById("form-cadastro");
  if (!form) return;

  const cpf = document.getElementById("cpf");
  const sucesso = document.getElementById("msg-sucesso-cadastro");

  cpf.addEventListener("input", () => {
    cpf.setCustomValidity(cpfValido(cpf.value) ? "" : "CPF inválido");
  });

  form.addEventListener("submit", (evento) => {
    evento.preventDefault();
    cpf.setCustomValidity(cpfValido(cpf.value) ? "" : "CPF inválido");

    let valido = validarCamposObrigatorios(form);

    ["sexo", "sexo-pet"].forEach((nome) => {
      const ok = grupoRadioValido(form, nome);
      form.querySelectorAll(`input[name="${nome}"]`).forEach((r) => r.classList.toggle("is-invalid", !ok));
      if (!ok) valido = false;
    });

    if (!valido) {
      const primeiroErro = form.querySelector(".is-invalid");
      if (primeiroErro) primeiroErro.focus();
      return;
    }

    form.reset();
    form.querySelectorAll(".is-valid, .is-invalid").forEach((el) => el.classList.remove("is-valid", "is-invalid"));
    sucesso.classList.remove("d-none");
    sucesso.scrollIntoView({ behavior: "smooth", block: "center" });
  });
}

/* ---------- Formulário de agendamento ---------- */

function iniciarCardsSelecao(form, nome, classeCard, idErro) {
  const radios = form.querySelectorAll(`input[name="${nome}"]`);
  const erro = document.getElementById(idErro);

  radios.forEach((radio) => {
    const card = radio.closest(`.${classeCard}`);

    radio.addEventListener("change", () => {
      radios.forEach((r) => r.closest(`.${classeCard}`).classList.remove("selecionado"));
      card.classList.add("selecionado");
      if (erro) erro.classList.add("d-none");
    });

    card.addEventListener("keydown", (evento) => {
      if (evento.key === "Enter" || evento.key === " ") {
        evento.preventDefault();
        radio.checked = true;
        radio.dispatchEvent(new Event("change"));
      }
    });
  });
}

function iniciarAgendamento() {
  const form = document.getElementById("form-agendamento");
  if (!form) return;

  const data = document.getElementById("ag-data");
  const campoEndereco = document.getElementById("campo-endereco-busca");
  const endereco = document.getElementById("ag-endereco");
  const sucesso = document.getElementById("msg-sucesso-agendamento");
  const resumo = document.getElementById("resumo-agendamento");

  data.min = hojeISO();

  iniciarCardsSelecao(form, "servico", "card-selecao", "erro-servico");
  iniciarCardsSelecao(form, "metodo", "card-metodo", "erro-metodo");

  form.querySelectorAll('input[name="metodo"]').forEach((radio) => {
    radio.addEventListener("change", () => {
      const telebusca = radio.value === "telebusca" && radio.checked;
      campoEndereco.classList.toggle("d-none", !telebusca);
      endereco.required = telebusca;
      endereco.setAttribute("aria-required", String(telebusca));
      if (!telebusca) endereco.classList.remove("is-invalid", "is-valid");
    });
  });

  data.addEventListener("change", () => {
    if (!data.value) return data.setCustomValidity("");
    const domingo = new Date(`${data.value}T12:00:00`).getDay() === 0;
    const passado = data.value < hojeISO();
    data.setCustomValidity(domingo || passado ? "Data inválida" : "");
  });

  form.addEventListener("submit", (evento) => {
    evento.preventDefault();
    data.dispatchEvent(new Event("change"));

    let valido = validarCamposObrigatorios(form);

    [["servico", "erro-servico"], ["metodo", "erro-metodo"]].forEach(([nome, idErro]) => {
      const ok = grupoRadioValido(form, nome);
      document.getElementById(idErro).classList.toggle("d-none", ok);
      if (!ok) valido = false;
    });

    if (!valido) return;

    const servico = SERVICOS[form.querySelector('input[name="servico"]:checked').value];
    const metodo = form.querySelector('input[name="metodo"]:checked').value;
    const pet = document.getElementById("ag-pet").value.trim();
    const horario = document.getElementById("ag-horario").value;

    resumo.innerHTML = "";
    [
      `Pet: ${pet}`,
      `Serviço: ${servico.nome} (${servico.preco})`,
      `Data: ${formatarDataISO(data.value)} às ${horario}`,
      `Atendimento: ${METODOS[metodo]}${metodo === "telebusca" ? ` em ${endereco.value.trim()}` : ""}`,
    ].forEach((linha) => {
      const p = document.createElement("p");
      p.className = "mb-1";
      p.textContent = linha;
      resumo.appendChild(p);
    });

    form.reset();
    form.querySelectorAll(".selecionado").forEach((el) => el.classList.remove("selecionado"));
    form.querySelectorAll(".is-valid, .is-invalid").forEach((el) => el.classList.remove("is-valid", "is-invalid"));
    campoEndereco.classList.add("d-none");
    endereco.required = false;
    sucesso.classList.remove("d-none");
    sucesso.scrollIntoView({ behavior: "smooth", block: "center" });
  });
}

/* ---------- Inicialização ---------- */

document.addEventListener("DOMContentLoaded", () => {
  atualizarAno();
  atualizarRelogios();
  setInterval(atualizarRelogios, 1000);
  iniciarPromocoes();
  iniciarNavbar();

  aplicarMascara("cpf", mascaraCPF);
  aplicarMascara("telefone", mascaraTelefone);
  aplicarMascara("ag-tel", mascaraTelefone);
  aplicarMascara("cep", mascaraCEP);

  iniciarCadastro();
  iniciarAgendamento();
});
