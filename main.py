print("Olá, Seja Bem-Vindo")
print("Faça Login Para Prosseguir..:")

users = []

def cadrastar():
    user = input("Usuário: ")
    key_user = input("Senha: ")
    
    users.append({
    "Usuário": user,
    "Senha": key_user
    })
        
def login():
    user = input("Usuário: ")
    key_user = input("Senha: ")
    
    for u in users:
        if u["Usuário"] == user and u["Senha"] == key_user:
            print("Ok! ")
            return
          
    print("Usuário Incorreto! ")
    
while True:
    print("1 Cadrastar: ")
    print("2 Login: ")
    print("3 Sair: ")
        
    es = input("Escolha: ")
    
    if es == "1":
        cadrastar()
    elif es == "2":
        login()
    elif es == "3" : 
        break
    else:
    	print("Usuário Inválido ")        
    
    