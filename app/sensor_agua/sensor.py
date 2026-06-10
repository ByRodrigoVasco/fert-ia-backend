import serial
import os

PORTA = 'COM6'
BAUD  = 115200

def _caminho_arquivo():
    pasta_data = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    return os.path.join(pasta_data, "sensor.txt")

def create_sensor_data():
    caminho = _caminho_arquivo()
    try:
        with serial.Serial(PORTA, BAUD, timeout=1) as ser:
            with open(caminho, 'a') as f:
                print("Lendo sensor... (Ctrl+C para voltar)")
                while True:
                    linha = ser.readline().decode().strip()
                    if linha and linha[0].isdigit():
                        f.write(linha + '\n')
                        f.flush()
                        print(" ", linha)
    except KeyboardInterrupt:
        print("\nLeitura encerrada.")
    except Exception as e:
        print(f"Erro: {e}")
