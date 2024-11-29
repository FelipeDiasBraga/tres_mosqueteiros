# Projeto de Boia para Monitoramento da Qualidade da Água

## Visão Geral
Este projeto envolve o desenvolvimento de uma boia para monitoramento da qualidade da água em ambientes aquáticos, como rios, lagos e reservatórios. A boia é equipada com sensores de pH, turbidez e condutividade, além de um módulo GPS para localização e um módulo LoRa para comunicação entre as boias. Uma das boias funciona como a boia principal, que envia os dados coletados para uma API usando conectividade WiFi.

## Componentes Utilizados
1. **Arduino Mega 2560** (ou similar)
2. **Módulo LoRa (ex: SX1278/RFM95)**
3. **Módulo GPS (ex: Neo-6M)**
4. **Sensor de pH**
5. **Sensor de Turbidez**
6. **Sensor de Condutividade**
7. **Placa Solar e Bateria para Alimentação**
8. **Antena para o Módulo LoRa**

## Objetivos
- **Monitorar a qualidade da água** através dos sensores de pH, turbidez e condutividade.
- **Coletar e transmitir dados** de qualidade da água e localização usando uma rede mesh LoRa.
- **Enviar dados para um servidor remoto** a partir de uma boia principal conectada via WiFi.
- **Operar de forma autônoma** por meio de alimentação solar e bateria, garantindo sustentabilidade em áreas remotas.

## Como Funciona
1. **Leitura dos Sensores**: Os sensores de pH, turbidez e condutividade realizam leituras constantes da qualidade da água e enviam esses dados para o Arduino Mega.
2. **Processamento e Comunicação**: O Arduino Mega processa os valores dos sensores e adiciona dados de localização obtidos pelo módulo GPS. Os dados são então transmitidos via LoRa para outras boias.
3. **Boia Principal e Envio de Dados**: A boia principal recebe os dados das outras boias e envia esses dados para uma API por meio de uma conexão WiFi, onde são armazenados e processados.

## Conexões do Circuito
- **Módulo LoRa**: Conectado aos pinos SPI e pinos de controle do Arduino Mega.
- **Módulo GPS**: Conectado aos pinos de comunicação Serial1 do Arduino Mega.
- **Sensores**: Conectados aos pinos analógicos para leitura dos valores de pH, turbidez e condutividade.
- **Placa Solar e Bateria**: Conectadas para alimentar todo o circuito de forma autônoma.

## Diagrama do Circuito
Conectar todos os módulos e sensores ao Arduino Mega conforme a descrição abaixo:
1. **Módulo LoRa**: MISO (pino 50), MOSI (pino 51), SCK (pino 52), NSS (pino 10), RST (pino 9), DIO0 (pino 2).
2. **Módulo GPS**: RX (pino 18 - Serial1 TX), TX (pino 19 - Serial1 RX).
3. **Sensores de Qualidade da Água**:
   - **Sensor de pH**: Pino A0.
   - **Sensor de Turbidez**: Pino A1.
   - **Sensor de Condutividade**: Pino A2.
4. **Placa Solar e Bateria**: Controlador de carga conectado à bateria e ao Arduino Mega.

## Fluxo de Trabalho
1. **Inicialização**: O sistema é alimentado por bateria e placa solar, garantindo operação contínua.
2. **Leitura e Processamento**: Arduino Mega realiza a leitura dos sensores e recebe dados do módulo GPS.
3. **Transmissão via LoRa**: Cada boia transmite seus dados via LoRa para a boia principal em uma rede mesh.
4. **Envio para API**: A boia principal envia os dados recebidos para a API usando conexão WiFi.
5. **Teste e Validação**: Todos os componentes devem ser testados em um protoboard antes da montagem definitiva.

## Requisitos de Hardware e Software
- **Hardware**: Arduino Mega, Módulo LoRa, GPS Neo-6M, Sensores de pH, Turbidez, Condutividade, Placa Solar, Bateria, Protoboard, Jumpers.
- **Software**:
  - **IDE Arduino**: Para programar o Arduino Mega.
  - **Bibliotecas Arduino**: `LoRa.h`, `TinyGPSPlus.h`, `SPI.h`.
  - **API**: Desenvolvida em Python Flask, para receber e armazenar os dados coletados.

## Requisitos do Projeto Python (API)
- **Python 3.7+**
- **Dependências** (arquivo `requirements.txt`):
  ```
  Flask==2.3.2
  Flask-SQLAlchemy==3.0.4
  ```
- **Comando para instalar as dependências**:
  ```bash
  pip install -r requirements.txt
  ```
- **Execução da API**:
  ```bash
  python app.py
  ```

## Considerações Finais
Este projeto visa garantir o monitoramento eficiente e contínuo da qualidade da água em ambientes remotos. A sustentabilidade é assegurada pelo uso de energia solar, e a conectividade mesh permite que as boias trabalhem em conjunto para fornecer dados precisos e abrangentes.

