from playwright.sync_api import Page, expect

from pages.navbar_component import NavbarComponent
from pages.tax_optimizer_page import TaxOptimizerPage


def test_otimizador_fiscal_exibe_melhor_opcao(
    logged_page: Page,
    navbar: NavbarComponent,
    tax_optimizer_page: TaxOptimizerPage,
):
    navbar.navegar_para_otimizador_fiscal()
    expect(tax_optimizer_page.secao).to_be_visible()
    tax_optimizer_page.simular_resgate("100")
    expect(tax_optimizer_page.tabela_otimizacao).to_be_visible(timeout=10000)
    expect(tax_optimizer_page.melhor_opcao).to_be_visible()
