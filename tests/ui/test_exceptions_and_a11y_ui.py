from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.login_modal_page import LoginModalPage
from pages.navbar_component import NavbarComponent
from pages.portfolio_page import PortfolioPage


def test_formulario_login_vazio_bloqueia_submissao(
    page: Page,
    base_url: str,
    navbar: NavbarComponent,
    login_modal: LoginModalPage,
):
    page.goto(base_url)
    navbar.clicar_entrar()
    login_modal.preencher_usuario("")
    login_modal.preencher_senha("")
    login_modal.submeter()
    expect(login_modal.container_modal).to_be_visible()
    expect(navbar.botao_sair).not_to_be_visible()


def test_aporte_negativo_exibe_erro(
    logged_page: Page,
    navbar: NavbarComponent,
    portfolio_page: PortfolioPage,
):
    navbar.navegar_para_carteira()
    portfolio_page.cadastrar_aporte("Poupança", "-1", "1", "30", "180")
    expect(portfolio_page.alerta_erro).to_be_visible(timeout=5000)


def test_elementos_basicos_de_acessibilidade(
    page: Page,
    base_url: str,
    navbar: NavbarComponent,
):
    page.goto(base_url)
    base_page = BasePage(page)
    expect(navbar.botao_entrar).to_have_accessible_name("Entrar no Sistema")
    assert base_page.total_imagens_sem_alt() == 0
    assert base_page.total_campos_sem_rotulo() == 0
