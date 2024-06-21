from datetime import datetime

now = datetime.now()
def dia_da_semana():
    '''
        Formato retorno:
        Segunda-feira: 0
        Terça-feira: 1
        Quarta-feira: 2
        Quinta-feira: 3
        Sexta-feira: 4
        Sábado: 5
        Domingo: 6
    '''
    numero_dia_semana = now.weekday()
    return numero_dia_semana

def semana_do_ano():
    semana = now.isocalendar()[1]  # Retorna uma tupla (ano_iso, semana_iso, dia_iso)
    return semana

def mes():
    mes = now.month
    return mes

def ano():
    ano = now.year
    return ano