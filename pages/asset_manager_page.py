from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class AssetManagerPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.secao = page.locator("[data-testid='section-asset-manager']")
        self.tabela_taxas = page.locator("[data-testid='table-asset-rates']")
        self.linhas_taxas = self.tabela_taxas.locator("tbody tr")
        self.mensagem_sucesso = page.locator(
            "[data-testid='section-asset-manager'] div"
        ).filter(has_text="sucesso").first

    def obter_primeira_linha(self) -> Locator:
        return self.linhas_taxas.first

    def obter_nome_ativo(self, linha: Locator) -> str:
        return linha.locator("td").nth(0).inner_text()

    def obter_taxa_salva(self, linha: Locator) -> str:
        return linha.locator("td").nth(2).inner_text().split("%")[0].strip()

    def alterar_taxa(self, linha: Locator, taxa: str):
        linha.locator("input").fill(taxa)
        linha.locator("button", has_text="Salvar Alteração").click()

    def obter_linha_por_ativo(self, nome_ativo: str) -> Locator:
        return self.linhas_taxas.filter(has_text=nome_ativo).first

    def obter_celula_taxa_salva(self, linha: Locator) -> Locator:
        return linha.locator("td").nth(2)
