from decimal import Decimal

from playwright.sync_api import Page, expect

from pages.asset_manager_page import AssetManagerPage
from pages.navbar_component import NavbarComponent


def test_visualizar_e_alterar_taxa_anual(
    logged_page: Page,
    navbar: NavbarComponent,
    asset_manager_page: AssetManagerPage,
):
    navbar.navegar_para_gerenciar_taxas()
    expect(asset_manager_page.secao).to_be_visible()
    expect(asset_manager_page.tabela_taxas).to_be_visible()
    linha = asset_manager_page.obter_primeira_linha()
    nome_ativo = asset_manager_page.obter_nome_ativo(linha)
    taxa_original = asset_manager_page.obter_taxa_salva(linha)
    nova_taxa = str(Decimal(taxa_original) + Decimal("0.01"))
    asset_manager_page.alterar_taxa(linha, nova_taxa)
    linha_atualizada = asset_manager_page.obter_linha_por_ativo(nome_ativo)
    celula_atualizada = asset_manager_page.obter_celula_taxa_salva(linha_atualizada)
    expect(celula_atualizada).to_contain_text(nova_taxa)
    asset_manager_page.alterar_taxa(linha_atualizada, taxa_original)
    linha_restaurada = asset_manager_page.obter_linha_por_ativo(nome_ativo)
    celula_restaurada = asset_manager_page.obter_celula_taxa_salva(linha_restaurada)
    expect(celula_restaurada).to_contain_text(taxa_original)
