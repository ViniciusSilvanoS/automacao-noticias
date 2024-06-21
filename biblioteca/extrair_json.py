def extrair_json(texto):
    # Essa função deve receber um STRING TEXTO / E retornará uma STRING JSON
    import re
    import json

    padrao = r'{[^{}]*}'
    resultados = re.findall(padrao, texto)
    if resultados:
        substring_json = [json.loads(resultado) for resultado in resultados]
        json = json.dumps(substring_json)

        return json
    else:
        return None