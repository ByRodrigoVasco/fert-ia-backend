# fert-ia-backend

Sistema de cadastro de usuários com leitura de sensor de água, em Python.

## Como rodar

​```bash
pip install pyserial
python main.py
​```

## Estrutura

​```
.
├── main.py                      # menu principal + cadastro
├── app/
│   ├── crud.py                  # operações de usuário (login, update, delete)
│   └── sensor.py                # leitura do sensor via porta serial
├── data/                        # arquivos de persistência (usuários e leituras)
└── water_sensor/                # firmware do ESP32
​```

## O que o programa faz

- Cadastrar, logar, mudar senha e excluir conta (dados em `data/usuarios.txt`).
- Após login, consultar o sensor de água ligado por USB (porta `COM6`, baud `115200`) e gravar leituras em `data/sensor.txt`.

## Equipe

Projeto acadêmico — CESAR School.
