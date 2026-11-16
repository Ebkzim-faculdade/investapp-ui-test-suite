from playwright.sync_api import Page

from pages.base_page import BasePage


class YieldSimulatorPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.secao = page.locator("[data-testid='section-yield-simulator']")
        self.input_meses = page.locator("[data-testid='input-sim-months']")
        self.botao_calcular = page.locator("[data-testid='btn-calc-monthly']")
        self.tabela_projecao = page.locator("[data-testid='table-monthly-projection']")
        self.tabela_resumo = page.locator("[data-testid='table-type-summary']")
        self.linhas_projecao = self.tabela_projecao.locator("tbody tr")

    def calcular_projecao(self, meses: str):
        self.input_meses.fill(meses)
        self.botao_calcular.click()
