def validar_rango_ip(func):
    def wrapper(*args, **kwargs):
        for ip in args:
            octetos = ip.split('.')
            if len(octetos) != 4:
                print(f"La dirección IP {ip} no tiene 4 octetos.")
                return
            for octeto in octetos:
                try:
                    valor = int(octeto)
                    if valor < 0 or valor > 255:
                        print(f"El octeto {octeto} en la dirección IP {ip} está fuera de rango.")
                        return
                except ValueError:
                    print(f"El octeto {octeto} en la dirección IP {ip} no es un número válido.")
                    return
        return func(*args, **kwargs)
    return wrapper

# Uso del decorador
@validar_rango_ip
def funcion_con_ips(*ips):
    # Tu función aquí
    print("Función ejecutada con éxito")

# Ejemplos de uso
funcion_con_ips("190.8.176.187", "256.0.0.1")

