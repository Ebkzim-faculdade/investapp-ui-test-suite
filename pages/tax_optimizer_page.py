from playwright.sync_api import Page

from pages.base_page import BasePage


class TaxOptimizerPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.secao = page.locator("[data-testid='section-tax-simulator']")
        self.input_valor_resgate = page.locator(
            "[data-testid='input-withdraw-amount']"
        )
        self.botao_calcular = page.locator("[data-testid='btn-calc-withdrawal']")
        self.tabela_otimizacao = page.locator(
            "[data-testid='table-tax-optimization']"
        )
        self.melhor_opcao = self.tabela_otimizacao.locator(".badge-best-option")

    def simular_resgate(self, valor: str):
        self.input_valor_resgate.fill(valor)
        self.botao_calcular.click()
