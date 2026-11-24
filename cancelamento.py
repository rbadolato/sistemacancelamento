from datetime import datetime, timedelta

nome = input("Nome do assinante: ")
plataforma = input("Nome da plataforma: ")
assinatura = input("Data de assinatura (DD/MM/AAAA): ")
cancelamento = input("Data da solicitação (DD/MM/AAAA): ")

assinatura = datetime.strptime (assinatura, "%d/%m/%Y").date()
cancelamento = datetime.strptime (cancelamento, "%d/%m/%Y").date()

dias_passados = (cancelamento - assinatura).days

if dias_passados < 0:
    print("ERRO: a data de cancelamento é anterior à data da compra.")

elif dias_passados > 7:
    print("Reembolso não autorizado.")

else: 
    print()
    print(f"Solicitação de {nome} dentro do prazo! Reembolso autorizado.")
    data_limite = cancelamento
    dias_uteis = 0
    
    while dias_uteis < 15:
       data_limite += timedelta(days=1)

       if data_limite.weekday () < 5:
        dias_uteis += 1
    
    print()
    print(f"Data limite para reembolso de {nome}: ", data_limite.strftime("%d/%m/%Y"))
    print()
    print("Plataforma:", plataforma)
    print("Data de assinatura:", assinatura)
    print("Data de cancelamento:", cancelamento)
