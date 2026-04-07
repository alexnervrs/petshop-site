<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cadastro - PetShop Amigo Fiel</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- NAVBAR -->
  <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="navbar-principal" role="navigation" aria-label="Menu de navegação principal">
    <div class="container">
      <a class="navbar-brand" href="index.html" aria-label="PetShop Amigo Fiel - Página inicial">
        <span class="brand-icone" aria-hidden="true">🐾</span> Amigo Fiel
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menuNav"
        aria-controls="menuNav" aria-expanded="false" aria-label="Abrir menu de navegação">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="menuNav">
        <ul class="navbar-nav ms-auto align-items-lg-center gap-lg-1">
          <li class="nav-item"><a class="nav-link nav-link-custom" href="index.html">Início</a></li>
          <li class="nav-item"><a class="nav-link nav-link-custom" href="produtos.html">Produtos</a></li>
          <li class="nav-item"><a class="nav-link nav-link-custom" href="servicos.html">Serviços</a></li>
          <li class="nav-item"><a class="nav-link nav-link-custom" href="contato.html">Contato</a></li>
          <li class="nav-item ms-lg-2"><a class="nav-link btn-destaque ativo" href="cadastro.html" aria-current="page"><i class="bi bi-person-plus-fill" aria-hidden="true"></i> Cadastro</a></li>
          <li class="nav-item ms-lg-1"><a class="nav-link btn-destaque btn-verde" href="agendamento.html"><i class="bi bi-calendar-check-fill" aria-hidden="true"></i> Agendar</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- CABEÇALHO -->
  <div class="cabecalho-pagina" role="banner">
    <div class="container text-center">
      <h1><i class="bi bi-person-plus-fill me-2" aria-hidden="true"></i>Cadastro de Cliente e Pet</h1>
      <p>Preencha os dados abaixo para se cadastrar no Amigo Fiel</p>
    </div>
  </div>

  <!-- FORMULÁRIO -->
  <main class="container py-5" id="conteudo" role="main">
    <div class="form-envoltorio mx-auto">

      <form id="form-cadastro" novalidate aria-label="Formulário de cadastro de cliente e pet">

        <!-- ===== DADOS DO TUTOR ===== -->
        <fieldset class="bloco-form mb-4">
          <legend class="titulo-bloco-form">
            <i class="bi bi-person-circle me-2" aria-hidden="true"></i>Dados do Tutor
          </legend>

          <div class="row g-3">

            <!-- Nome completo -->
            <div class="col-md-6">
              <label for="nome" class="form-label">
                Nome completo <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="text"
                class="form-control"
                id="nome"
                name="nome"
                placeholder="Ex.: Maria da Silva"
                required
                aria-required="true"
                aria-describedby="nome-ajuda"
                autocomplete="name"
              >
              <div id="nome-ajuda" class="form-text">Informe o nome completo conforme documento.</div>
              <div class="invalid-feedback">Por favor, informe seu nome completo.</div>
            </div>

            <!-- CPF -->
            <div class="col-md-6">
              <label for="cpf" class="form-label">
                CPF <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="text"
                class="form-control"
                id="cpf"
                name="cpf"
                placeholder="000.000.000-00"
                maxlength="14"
                required
                aria-required="true"
                aria-describedby="cpf-ajuda"
                autocomplete="off"
              >
              <div id="cpf-ajuda" class="form-text">Somente números — a formatação é automática.</div>
              <div class="invalid-feedback">Informe um CPF válido (11 dígitos).</div>
            </div>

            <!-- Data de nascimento -->
            <div class="col-md-4">
              <label for="data-nasc" class="form-label">
                Data de nascimento <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="date"
                class="form-control"
                id="data-nasc"
                name="dataNasc"
                required
                aria-required="true"
                autocomplete="bday"
              >
              <div class="invalid-feedback">Informe sua data de nascimento.</div>
            </div>

            <!-- Sexo -->
            <div class="col-md-4">
              <label class="form-label d-block">
                Sexo <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <div class="d-flex gap-3 pt-2" role="radiogroup" aria-label="Selecione o sexo" aria-required="true">
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="sexo" id="sexo-m" value="M" required>
                  <label class="form-check-label" for="sexo-m">Masculino</label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="sexo" id="sexo-f" value="F">
                  <label class="form-check-label" for="sexo-f">Feminino</label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="sexo" id="sexo-o" value="O">
                  <label class="form-check-label" for="sexo-o">Outro</label>
                </div>
              </div>
            </div>

            <!-- Telefone -->
            <div class="col-md-4">
              <label for="telefone" class="form-label">
                Telefone / WhatsApp <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="tel"
                class="form-control"
                id="telefone"
                name="telefone"
                placeholder="(85) 9 9999-9999"
                maxlength="16"
                required
                aria-required="true"
                autocomplete="tel"
              >
              <div class="invalid-feedback">Informe um telefone com DDD.</div>
            </div>

            <!-- E-mail -->
            <div class="col-md-6">
              <label for="email" class="form-label">
                E-mail <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="email"
                class="form-control"
                id="email"
                name="email"
                placeholder="seuemail@exemplo.com"
                required
                aria-required="true"
                autocomplete="email"
              >
              <div class="invalid-feedback">Informe um e-mail válido.</div>
            </div>

            <!-- CEP -->
            <div class="col-md-3">
              <label for="cep" class="form-label">
                CEP <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="text"
                class="form-control"
                id="cep"
                name="cep"
                placeholder="60000-000"
                maxlength="9"
                required
                aria-required="true"
                autocomplete="postal-code"
              >
              <div class="invalid-feedback">Informe o CEP.</div>
            </div>

            <!-- Endereço -->
            <div class="col-md-9">
              <label for="endereco" class="form-label">
                Endereço <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="text"
                class="form-control"
                id="endereco"
                name="endereco"
                placeholder="Rua, número, bairro, cidade – UF"
                required
                aria-required="true"
                autocomplete="street-address"
              >
              <div class="invalid-feedback">Informe o endereço completo.</div>
            </div>

          </div>
        </fieldset>

        <!-- ===== DADOS DO PET ===== -->
        <fieldset class="bloco-form mb-4">
          <legend class="titulo-bloco-form">
            <i class="bi bi-heart-fill me-2" aria-hidden="true"></i>Dados do Pet
          </legend>

          <div class="row g-3">

            <!-- Nome do pet -->
            <div class="col-md-4">
              <label for="nome-pet" class="form-label">
                Nome do pet <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="text"
                class="form-control"
                id="nome-pet"
                name="nomePet"
                placeholder="Ex.: Bolinha"
                required
                aria-required="true"
              >
              <div class="invalid-feedback">Informe o nome do pet.</div>
            </div>

            <!-- Espécie -->
            <div class="col-md-4">
              <label for="especie" class="form-label">
                Espécie <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <select class="form-select" id="especie" name="especie" required aria-required="true">
                <option value="">Selecione…</option>
                <option value="cao">Cachorro</option>
                <option value="gato">Gato</option>
                <option value="outro">Outro</option>
              </select>
              <div class="invalid-feedback">Selecione a espécie do pet.</div>
            </div>

            <!-- Raça -->
            <div class="col-md-4">
              <label for="raca" class="form-label">
                Raça <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="text"
                class="form-control"
                id="raca"
                name="raca"
                placeholder="Ex.: Poodle, SRD…"
                required
                aria-required="true"
              >
              <div class="invalid-feedback">Informe a raça do pet.</div>
            </div>

            <!-- Sexo do pet -->
            <div class="col-md-3">
              <label class="form-label d-block">
                Sexo do pet <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <div class="d-flex gap-3 pt-2" role="radiogroup" aria-label="Sexo do pet" aria-required="true">
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="sexo-pet" id="pet-m" value="M" required>
                  <label class="form-check-label" for="pet-m">Macho</label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="radio" name="sexo-pet" id="pet-f" value="F">
                  <label class="form-check-label" for="pet-f">Fêmea</label>
                </div>
              </div>
            </div>

            <!-- Idade -->
            <div class="col-md-3">
              <label for="idade-pet" class="form-label">
                Idade (anos) <span class="campo-obrigatorio" aria-hidden="true">*</span>
              </label>
              <input
                type="number"
                class="form-control"
                id="idade-pet"
                name="idadePet"
                min="0"
                max="30"
                placeholder="Ex.: 3"
                required
                aria-required="true"
              >
              <div class="invalid-feedback">Informe a idade em anos (0 a 30).</div>
            </div>

            <!-- Peso -->
            <div class="col-md-3">
              <label for="peso-pet" class="form-label">Peso (kg)</label>
              <input
                type="number"
                class="form-control"
                id="peso-pet"
                name="pesoPet"
                min="0.1"
                max="100"
                step="0.1"
                placeholder="Ex.: 5.5"
              >
            </div>

            <!-- Porte -->
            <div class="col-md-3">
              <label for="porte" class="form-label">Porte</label>
              <select class="form-select" id="porte" name="porte">
                <option value="">Selecione…</option>
                <option value="mini">Mini (até 4 kg)</option>
                <option value="pequeno">Pequeno (4–10 kg)</option>
                <option value="medio">Médio (10–25 kg)</option>
                <option value="grande">Grande (25+ kg)</option>
              </select>
            </div>

            <!-- Observações -->
            <div class="col-12">
              <label for="obs-pet" class="form-label">Observações de saúde</label>
              <textarea
                class="form-control"
                id="obs-pet"
                name="obsPet"
                rows="3"
                placeholder="Alergias, medicamentos, comportamento especial…"
                aria-describedby="obs-ajuda"
              ></textarea>
              <div id="obs-ajuda" class="form-text">Informe qualquer condição relevante para o atendimento do pet.</div>
            </div>

            <!-- Serviços de interesse -->
            <div class="col-12">
              <label class="form-label d-block">Serviços de interesse</label>
              <div class="d-flex flex-wrap gap-3" role="group" aria-label="Marque os serviços de interesse">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="int-banho" name="interesse" value="banho">
                  <label class="form-check-label" for="int-banho">Banho</label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="int-tosa" name="interesse" value="tosa">
                  <label class="form-check-label" for="int-tosa">Tosa</label>
                </div>
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="int-ambos" name="interesse" value="ambos">
                  <label class="form-check-label" for="int-ambos">Banho + Tosa</label>
                </div>
              </div>
            </div>

          </div>
        </fieldset>

        <!-- Termos -->
        <div class="mb-4">
          <div class="form-check">
            <input class="form-check-input" type="checkbox" id="aceita-termos" name="aceitaTermos" required aria-required="true">
            <label class="form-check-label" for="aceita-termos">
              Concordo com os <a href="#" aria-label="Ver termos e condições">Termos e Condições</a>
              e autorizo o uso dos meus dados para contato e agendamento.
              <span class="campo-obrigatorio" aria-hidden="true">*</span>
            </label>
            <div class="invalid-feedback">Você precisa aceitar os termos para continuar.</div>
          </div>
        </div>

        <!-- Botões -->
        <div class="text-center d-flex flex-wrap gap-3 justify-content-center">
          <button type="submit" class="btn-principal" aria-label="Enviar formulário de cadastro">
            <i class="bi bi-check-circle-fill me-2" aria-hidden="true"></i>Finalizar Cadastro
          </button>
          <a href="index.html" class="btn-secundario" aria-label="Cancelar e voltar à página inicial">
            Cancelar
          </a>
        </div>

      </form>

      <!-- Mensagem de sucesso (oculta até o envio) -->
      <div id="msg-sucesso-cadastro" class="alerta-sucesso mt-4 d-none" role="alert" aria-live="assertive">
        <i class="bi bi-check-circle-fill me-2" aria-hidden="true"></i>
        <strong>Cadastro realizado com sucesso!</strong>
        Em breve entraremos em contato.
        Que tal <a href="agendamento.html">agendar um serviço</a> agora?
      </div>

    </div>
  </main>

  <!-- FOOTER -->
  <footer class="rodape py-4" role="contentinfo">
    <div class="container text-center">
      <p class="mb-1"><strong>PetShop Amigo Fiel</strong> — Rua Tavares, 234, Complemento 01 — Fortaleza, CE</p>
      <p class="mb-0 rodape-copy">Site desenvolvido por Alex &mdash; &copy; <span id="ano-atual"></span></p>
    </div>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="script.js"></script>
</body>
</html>