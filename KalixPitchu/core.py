#codigo install.shlar.sh
import os
import sys
import webbrowser
from platform import system
from traceback import print_exc
from typing import Callable, List, Tuple

def limpar_tela():
    """Limpa a tela do terminal com base no sistema operacional."""
    os.system("cls" if system() == "Windows" else "clear")

def validar_entrada(ip, intervalo_val):
    """Valida a entrada do usuário, garantindo que seja um número inteiro dentro de um intervalo."""
    intervalo_val = intervalo_val or []
    try:
        ip = int(ip)
        if ip in intervalo_val:
            return ip
    except Exception:
        return None
    return None

class FerramentaDeHacking:
    """Classe base para uma ferramenta de hacking."""

    TITULO: str = ""  # Usado para mostrar informações no menu
    DESCRICAO: str = ""
    COMANDOS_DE_INSTALACAO: List[str] = []
    DIRETORIO_DE_INSTALACAO: str = ""
    COMANDOS_DE_DESINSTALACAO: List[str] = []
    COMANDOS_DE_EXECUCAO: List[str] = []
    OPCOES: List[Tuple[str, Callable]] = []
    URL_PROJETO: str = ""

    def __init__(self, opcoes=None, instalavel: bool = True, executavel: bool = True):
        """Inicializa a ferramenta com opções de instalação e execução."""
        opcoes = opcoes or []
        if isinstance(opcoes, list):
            self.OPCOES = []
            if instalavel:
                self.OPCOES.append(('Instalar', self.instalar))
            if executavel:
                self.OPCOES.append(('Executar', self.executar))
            self.OPCOES.extend(opcoes)
        else:
            raise Exception("As opções devem ser uma lista de tuplas (nome_opcao, funcao_opcao)")

    def mostrar_informacoes(self):
        """Exibe informações sobre a ferramenta, incluindo a descrição e URL do projeto."""
        descricao = self.DESCRICAO
        if self.URL_PROJETO:
            descricao += '\n\t[*] '
            descricao += self.URL_PROJETO
        os.system(f'echo "{descricao}"|boxes -d boy | lolcat')

    def mostrar_opcoes(self, pai=None):
        """Mostra as opções disponíveis e processa a entrada do usuário."""
        limpar_tela()
        self.mostrar_informacoes()
        for indice, opcao in enumerate(self.OPCOES):
            print(f"[{indice + 1}] {opcao[0]}")
        if self.URL_PROJETO:
            print(f"[{98}] Abrir página do projeto")
        print(f"[{99}] Voltar para {pai.TITULO if pai is not None else 'Sair'}")
        indice_opcao = input("Selecione uma opção: ").strip()
        try:
            indice_opcao = int(indice_opcao)
            if indice_opcao - 1 in range(len(self.OPCOES)):
                codigo_retorno = self.OPCOES[indice_opcao - 1][1]()
                if codigo_retorno != 99:
                    input("\n\nPressione ENTER para continuar:").strip()
            elif indice_opcao == 98:
                self.mostrar_pagina_projeto()
            elif indice_opcao == 99:
                if pai is None:
                    sys.exit()
                return 99
        except (TypeError, ValueError):
            print("Por favor, insira uma opção válida")
            input("\n\nPressione ENTER para continuar:").strip()
        except Exception:
            print_exc()
            input("\n\nPressione ENTER para continuar:").strip()
        return self.mostrar_opcoes(pai=pai)

    def antes_de_instalar(self):
        """Método para ser sobrescrito antes da instalação."""
        pass

    def instalar(self):
        """Instala a ferramenta executando comandos de instalação."""
        self.antes_de_instalar()
        if isinstance(self.COMANDOS_DE_INSTALACAO, (list, tuple)):
            for comando_instalacao in self.COMANDOS_DE_INSTALACAO:
                os.system(comando_instalacao)
            self.depois_de_instalar()

    def depois_de_instalar(self):
        """Método para ser sobrescrito após a instalação."""
        print("Instalação concluída com sucesso!")

    def antes_de_desinstalar(self) -> bool:
        """Pede confirmação ao usuário e retorna se a desinstalação deve prosseguir."""
        return True

    def desinstalar(self):
        """Desinstala a ferramenta executando comandos de desinstalação."""
        if self.antes_de_desinstalar():
            if isinstance(self.COMANDOS_DE_DESINSTALACAO, (list, tuple)):
                for comando_desinstalacao in self.COMANDOS_DE_DESINSTALACAO:
                    os.system(comando_desinstalacao)
            self.depois_de_desinstalar()

    def depois_de_desinstalar(self):
        """Método para ser sobrescrito após a desinstalação."""
        pass

    def antes_de_executar(self):
        """Método para ser sobrescrito antes da execução."""
        pass

    def executar(self):
        """Executa a ferramenta executando comandos definidos."""
        self.antes_de_executar()
        if isinstance(self.COMANDOS_DE_EXECUCAO, (list, tuple)):
            for comando_execucao in self.COMANDOS_DE_EXECUCAO:
                os.system(comando_execucao)
            self.depois_de_executar()

    def depois_de_executar(self):
        """Método para ser sobrescrito após a execução."""
        pass

    def esta_instalada(self, diretorio_para_checar=None):
        """Método não implementado para verificar se a ferramenta está instalada."""
        print("Não implementado: NÃO USE")
        return "?"

    def mostrar_pagina_projeto(self):
        """Abre a página do projeto no navegador web."""
        webbrowser.open_new_tab(self.URL_PROJETO)

class ColecaoDeFerramentas:
    """Classe que gerencia uma coleção de ferramentas de hacking."""

    TITULO: str = ""  # Usado para mostrar informações no menu
    DESCRICAO: str = ""
    FERRAMENTAS = []  # Lista de ferramentas (FerramentaDeHacking ou ColecaoDeFerramentas)

    def __init__(self):
        """Inicializa a coleção de ferramentas."""
        pass

    def mostrar_informacoes(self):
        """Exibe informações sobre a coleção de ferramentas usando figlet."""
        os.system("figlet -f standard -c {} | lolcat".format(self.TITULO))
        # os.system(f'echo "{self.DESCRICAO}"|boxes -d boy | lolcat')
        # print(self.DESCRICAO)

    def mostrar_opcoes(self, pai=None):
        """Mostra as opções disponíveis na coleção e processa a entrada do usuário."""
        limpar_tela()
        self.mostrar_informacoes()
        for indice, ferramenta in enumerate(self.FERRAMENTAS):
            print(f"[{indice}] {ferramenta.TITULO}")
        print(f"[{99}] Voltar para {pai.TITULO if pai is not None else 'Sair'}")
        indice_ferramenta = input("Escolha uma ferramenta para prosseguir: ").strip()
        try:
            indice_ferramenta = int(indice_ferramenta)
            if indice_ferramenta in range(len(self.FERRAMENTAS)):
                codigo_retorno = self.FERRAMENTAS[indice_ferramenta].mostrar_opcoes(pai=self)
                if codigo_retorno != 99:
                    input("\n\nPressione ENTER para continuar:").strip()
            elif indice_ferramenta == 99:
                if pai is None:
                    sys.exit()
                return 99
        except (TypeError, ValueError):
            print("Por favor, insira uma opção válida")
            input("\n\nPressione ENTER para continuar:").strip()
        except Exception:
            print_exc()
            input("\n\nPressione ENTER para continuar:").strip()
        return self.mostrar_opcoes(pai=pai)