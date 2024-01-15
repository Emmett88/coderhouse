from plyer import notification
import datetime

def alerta(nivel, base, etapa):
    # níveis do alerta
    titulos = {
        1: "Alerta Baixo",
        2: "Alerta Médio",
        3: "Alerta Alto"
    }
    
    # OQue horas rolou o B.O
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Mensagem do alerta
    mensagem = f"Cagou o carregamendo dos dados da base, mano da quebrada! {base} Foi na fase {etapa} - {data_atual}"
    
    # Como vai aparecer a notificação
    notification.notify(
        title=titulos[nivel],  # Título do alerta
        message=mensagem,      # Mensagem do alerta
        app_name="Alerta que deu merda"  # Nome do aplicativo
        # Você pode adicionar outros parâmetros conforme necessário
    )

# Exemplo de uso da função:
alerta(nivel=2, base="CLIENTES", etapa="EXTRAÇÃO DA BAGAÇA DO BAGUIO!")
