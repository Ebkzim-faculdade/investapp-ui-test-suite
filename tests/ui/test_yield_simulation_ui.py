from playwright.sync_api import Page, expect

from pages.navbar_component import NavbarComponent
from pages.yield_simulator_page import YieldSimulatorPage


def test_simular_rentabilidade_mes_a_mes(
    logged_page: Page,
    navbar: NavbarComponent,
    yield_simulator_page: YieldSimulatorPage,
):
    navbar.navegar_para_simulador()
    expect(yield_simulator_page.secao).to_be_visible()
    yield_simulator_page.calcular_projecao("3")
    expect(yield_simulator_page.tabela_projecao).to_be_visible(timeout=10000)
    expect(yield_simulator_page.tabela_resumo).to_be_visible()
    expect(yield_simulator_page.linhas_projecao).to_have_count(3)
