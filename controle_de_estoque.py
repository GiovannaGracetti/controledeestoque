# SISTEMA DE CONTROLE DE ESTOQUE
# =========================================
# Mercado Central
# Data: 19/05/2026
# Giovanna Gracetti
# SUPERMERCADO AURORA

# IMPORTAÇÃO DAS BIBLIOTECAS
import os
import locale #moeda brasileira
from tabulate import tabulate #tabelas
import pwinput #para mascarar a senha com "*"

try:
    import msvcrt
    WINDOWS = True
except ImportError:
    import tty
    import termios
    WINDOWS = False

try:
    if WINDOWS:
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    else:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')

# LISTA E DICIONÁRIO
L0 = []
D1 = {}
# LEITURA DO ARQUIVO TXT
try:
    with open("Dados.txt", "r", encoding="utf-8") as Dados:
        for i in Dados:
            L0.append(i.rstrip().split(","))
# TRANSFORMA LISTA EM DICIONÁRIO    
    for i in L0:
        if len(i) == 5:
            D1[i[0]] = [
                i[1],            # Produto
                i[2],            # Setor
                float(i[3]),     # Preço
                int(i[4])        # Quantidade
            ]
except FileNotFoundError:
    open("Dados.txt", "w").close()

# LOGIN E SENHA
usuario_C = "MercadoAurora"
senha_C = "Aurora26@"

def limpar():
    if WINDOWS:
        os.system('cls')
    else:
        os.system('clear')
        print("c", end="")

def titulo(texto):
    print('=' * 100)
    print(texto.center(100))
    print('=' * 100)

def ler_tecla():
    if WINDOWS:
        tecla = msvcrt.getch()

        if tecla == b'\xe0':
            tecla2 = msvcrt.getch()

            if tecla2 == b'H':
                return "UP"
            elif tecla2 == b'P':
                return "DOWN"

        elif tecla == b'\r':
            return "ENTER"

    else:
        fd = os.sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            tecla = os.read(fd, 3)

            if tecla == b'\x1b[A':
                return "UP"
            elif tecla == b'\x1b[B':
                return "DOWN"
            elif tecla in (b'\r', b'\n'):
                return "ENTER"
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   
def login():
    tentativas = 3
    while tentativas > 0:
        limpar()
        titulo(r'''
╔═╗╦╔═╗╔╦╗╔═╗╔╦╗╔═╗  ╔═╗╦ ╦╦═╗╔═╗╦═╗╔═╗       ╔═╗╔╗╔╔╦╗╦═╗╔═╗  ╔═╗╔═╗╔╦╗  ╔═╗╔═╗╦ ╦  ╦  ╔═╗╔═╗╦╔╗╔
╚═╗║╚═╗ ║ ║╣ ║║║╠═╣  ╠═╣║ ║╠╦╝║ ║╠╦╝╠═╣  ───  ║╣ ║║║ ║ ╠╦╝║╣   ║  ║ ║║║║  ╚═╗║╣ ║ ║  ║  ║ ║║ ╦║║║║
╚═╝╩╚═╝ ╩ ╚═╝╩ ╩╩ ╩  ╩ ╩╚═╝╩╚═╚═╝╩╚═╩ ╩       ╚═╝╝╚╝ ╩ ╩╚═╚═╝  ╚═╝╚═╝╩ ╩  ╚═╝╚═╝╚═╝  ╩═╝╚═╝╚═╝╩╝╚╝
               ''' )
        usuario = input("\nLogin: ")
        senha = pwinput.pwinput("Senha: ", mask="*")
        if usuario == usuario_C and senha == senha_C:
            print("\nBEM VINDO")
            input("\nPressione ENTER para iniciar sistema")
            return True
        else:
            tentativas -= 1
            print ("\nLogin inválido")
            print (f"Tentativas restantes: {tentativas}")
            input ("Pressione ENTER para tentar novamente")
    print ("\nMUITAS TENTATIVAS - sistema bloqueado")
    return False
if not login():
    exit()
menu = [
    "[1] Pesquisar Código",
    "[2] Pesquisar Setor",
    "[3] Listar Produtos",
    "[4] Incluir Produto",
    "[5] Alterar Produto",
    "[6] Deletar Produto",
    "[S] Finalizar Sistema"
]
# OPÇÕES INTERNAS
opcoes = ["1", "2", "3", "4", "5", "6", "S"]
# POSIÇÃO DO CURSOR
posicao = 0
# FUNÇÃO LIMPAR TELA
def limpar():
    if WINDOWS:
        os.system('cls')
    else:
        os.system('clear')
        print("c", end="")
# FUNÇÃO TÍTULO
def titulo(texto):
    print('=' * 100)
    print(texto.center(100))
    print('=' * 100)
# FUNÇÃO SALVAR TXT
def salvar_txt():
    with open("Dados.txt", "w", encoding="utf-8") as Dados:
        for ch, db in D1.items():
            Dados.write(
                f"{ch},{db[0]},{db[1]},{db[2]},{db[3]}\n"
            )

# LOOPING - PARA VOLTAR SEMPRE PARA O MENU
while True:
    limpar()
    titulo(r'''
╔═╗╔═╗╔╗╔╔╦╗╦═╗╔═╗╦  ╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╔╦╗╔═╗╔═╗ ╦ ╦╔═╗       ╔╦╗╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗  ╔═╗╦ ╦╦═╗╔═╗╦═╗╔═╗
║  ║ ║║║║ ║ ╠╦╝║ ║║  ║╣    ║║║╣   ║╣ ╚═╗ ║ ║ ║║═╬╗║ ║║╣   ───  ║║║║╣ ╠╦╝║  ╠═╣ ║║║ ║  ╠═╣║ ║╠╦╝║ ║╠╦╝╠═╣
╚═╝╚═╝╝╚╝ ╩ ╩╚═╚═╝╩═╝╚═╝  ═╩╝╚═╝  ╚═╝╚═╝ ╩ ╚═╝╚═╝╚╚═╝╚═╝       ╩ ╩╚═╝╩╚═╚═╝╩ ╩═╩╝╚═╝  ╩ ╩╚═╝╩╚═╚═╝╩╚═╩ ╩          
 ''')
    print("Use as SETAS do teclado e ENTER para selecionar\n")

# EXIBIÇÃO DO MENU
    for i in range(len(menu)):
        if i == posicao:
         print(f"► {menu[i]}")
        else:
         print(f"  {menu[i]}")

# FAZENDO A TECLA FUNCIONAR 
    tecla = ler_tecla()
    if tecla == "UP":
        posicao -= 1
        if posicao < 0:
            posicao = len(menu) - 1
    elif tecla == "DOWN":
        posicao += 1
        if posicao >= len(menu):
            posicao = 0
    elif tecla == "ENTER":
        opt = opcoes[posicao]
        limpar()

# OPÇÃO 1 - PESQUISAR CÓDIGO    
        if opt == "1":
            titulo(r'''
╔═╗╔═╗╔═╗╔═╗ ╦ ╦╦╔═╗╔═╗╦═╗  ╔═╗╔═╗╔╦╗╦╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔╦╗╔═╗
╠═╝║╣ ╚═╗║═╬╗║ ║║╚═╗╠═╣╠╦╝  ║  ║ ║ ║║║║ ╦║ ║  |║║║ ║  ╠═╝╠╦╝║ ║ ║║║ ║ ║ ║ ║
╩  ╚═╝╚═╝╚═╝╚╚═╝╩╚═╝╩ ╩╩╚═  ╚═╝╚═╝═╩╝╩╚═╝╚═╝  ═╩╝╚═╝  ╩  ╩╚═╚═╝═╩╝╚═╝ ╩ ╚═╝''')
            codigo = input("Digite o código: ")
            if codigo in D1:
                db = D1[codigo]
                print("\nPRODUTO ENCONTRADO\n")
                print(f"Código: {codigo}")
                print(f"Produto: {db[0]}")
                print(f"Setor: {db[1]}")
                print(f"Preço: {locale.currency(db[2], grouping=True)}")
                print(f"Quantidade: {db[3]}")
                input("\nPressione ENTER para voltar")
            else:
                print("\nProduto não encontrado!")
                input("\nPressione ENTER para voltar")
# OPÇÃO 2 - PESQUISAR SETOR
        elif opt == "2":
            titulo(r'''
╔═╗╔═╗╔═╗╔═╗ ╦ ╦╦╔═╗╔═╗╦═╗  ╔═╗╔═╗╔╦╗╔═╗╦═╗                                                                                                     
╠═╝║╣ ╚═╗║═╬╗║ ║║╚═╗╠═╣╠╦╝  ╚═╗║╣  ║ ║ ║╠╦╝                                                                                                     
╩  ╚═╝╚═╝╚═╝╚╚═╝╩╚═╝╩ ╩╩╚═  ╚═╝╚═╝ ╩ ╚═╝╩╚''')
            setor = input("Digite o setor: ")
            tabela = []
            for ch, db in D1.items():
                if db[1].lower() == setor.lower():
                    tabela.append([
                        ch,
                        db[0],
                        db[1],
                        locale.currency(db[2], grouping=True),
                        db[3]
                    ])
            if tabela:
                cabecalho = [
                    "Código",
                    "Produto",
                    "Setor",
                    "Preço",
                    "Quantidade"
                ]
                print(
                    tabulate(
                        tabela,
                        headers=cabecalho,
                        tablefmt="rounded_grid"
                    )
                )
                input("\nPressione ENTER para voltar")
            else:
                print("\nNenhum setor encontrado")
                input("\nPressione ENTER para voltar")
# OPÇÃO 3 - LISTAR PRODUTOS
        elif opt == "3":
            titulo(r'''
╦  ╦╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔╦╗╔═╗╔═╗                                                                                                 
║  ║╚═╗ ║ ╠═╣   ║║║╣   ╠═╝╠╦╝║ ║ ║║║ ║ ║ ║ ║╚═╗                                                                                                 
╩═╝╩╚═╝ ╩ ╩ ╩  ═╩╝╚═╝  ╩  ╩╚═╚═╝═╩╝╚═╝ ╩ ╚═╝╚═╝ ''')
            tabela = []
            for ch, db in D1.items():
                tabela.append([
                    ch,
                    db[0],
                    db[1],
                    locale.currency(db[2], grouping=True),
                    db[3]
                ])
            cabecalho = [
                "Código",
                "Produto",
                "Setor",
                "Preço",
                "Quantidade"
            ]
            print(
                tabulate(
                    tabela,
                    headers=cabecalho,
                    tablefmt="rounded_grid")
                )
            print(f"\nTotal de produtos cadastrados: {len(D1)}")
            input("\nPressione ENTER para voltar")
# OPÇÃO 4 - INCLUIR PRODUTO
        elif opt == "4":
            titulo(r'''
╔═╗╔═╗╔╦╗╔═╗╔═╗╔╦╗╦═╗╔═╗  ╔╦╗╔═╗  ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔╦╗╔═╗                                                                                         
║  ╠═╣ ║║╠═╣╚═╗ ║ ╠╦╝║ ║   ║║║╣   ╠═╝╠╦╝║ ║ ║║║ ║ ║ ║ ║                                                                                         
╚═╝╩ ╩═╩╝╩ ╩╚═╝ ╩ ╩╚═╚═╝  ═╩╝╚═╝  ╩  ╩╚═╚═╝═╩╝╚═╝ ╩ ╚═╝ ''')  
            codigo = input("Código: ")
            if codigo in D1:
                print("\nEste código já está cadastrado")
                input("Pressione ENTER para voltar")
            else:
                produto = input("Produto: ")
                setor = input("Setor: ")
                try:
                    preco = float(input("Preço: "))
                    quantidade = int(input("Quantidade: "))
                    D1[codigo] = [
                    produto,
                    setor,
                    preco,
                    quantidade
                    ]
                    salvar_txt()
                    print("\nProduto cadastrado com sucesso")
                    input("Pressione ENTER para voltar")
                except ValueError:
                    print("\n[ERRO]: Digite apenas NÚMEROS no preço (ex: 5.50) e na quantidade (ex:10)")
                    input("Precione ENTER para voltar e tentar novamente")
# OPÇÃO 5 - ALTERAR PRODUTO
        elif opt == "5":
            titulo(r'''
╔═╗╦ ╔╦╗╔═╗╦═╗╔═╗╦═╗  ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔╦╗╔═╗                                                                                                     
╠═╣║  ║ ║╣ ╠╦╝╠═╣╠╦╝  ╠═╝╠╦╝║ ║ ║║║ ║ ║ ║ ║                                                                                                     
╩ ╩╩═╝╩ ╚═╝╩╚═╩ ╩╩╚═  ╩  ╩╚═╚═╝═╩╝╚═╝ ╩ ╚═╝ ''')                                                                                                                                                                                                                                                   
            codigo = input("Código do prduto que deseja alterar: ")
            if codigo in D1:
                print ("\nCódigo encontrado")
                produto = input("Novo produto: ")
                setor = input("Setor: ")
                preco = input("Preço: ")
                quantidade = input("Quantidade: ")

                D1[codigo] = [
                    produto,
                    setor,
                    preco,
                    quantidade
                ]
                salvar_txt()
                print("\nProduto cadastrado com sucesso")
                input("\nPressione ENTER para voltar")
            else:
                print("\nProduto não enontrado")
                input("\nPressione ENTER para voltar")
# OPÇÃO 6 - DELETAR PRODUTO
        elif opt == "6":
            titulo(r'''
╔╦╗╔═╗╦  ╔═╗╔╦╗╔═╗╦═╗  ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔╦╗╔═╗                                                                                                    
 ║║║╣ ║  ║╣  ║ ╠═╣╠╦╝  ╠═╝╠╦╝║ ║ ║║║ ║ ║ ║ ║                                                                                                    
═╩╝╚═╝╩═╝╚═╝ ╩ ╩ ╩╩╚═  ╩  ╩╚═╚═╝═╩╝╚═╝ ╩ ╚═╝ ''')                                                                                                                                                                                                                                                  
            codigo = input("Código do produto que deseja deletar: ")
            if codigo in D1:
                del D1[codigo]
                salvar_txt()
                print("\nProduto deletado com sucesso")
                input("\nPressione ENTER para voltar")
            else:
                print("\nProduto não encontrado")
                input("\nPressione ENTER para voltar")
# OPÇÃO S - FINALIZAR SISTEMA
        elif opt.upper() == "S":
            titulo(f'''
╔═╗╔╗╔╔═╗╔═╗╦═╗╦═╗╔═╗╔╗╔╔╦╗╔═╗  ╔═╗╦╔═╗╔╦╗╔═╗╔╦╗╔═╗                                                                                             
║╣ ║║║║  ║╣ ╠╦╝╠╦╝╠═╣║║║ ║║║ ║  ╚═╗║╚═╗ ║ ║╣ ║║║╠═╣                                                                                             
╚═╝╝╚╝╚═╝╚═╝╩╚═╩╚═╩ ╩╝╚╝═╩╝╚═╝  ╚═╝╩╚═╝ ╩ ╚═╝╩ ╩╩ ╩''')
            break
