#include <TFT_eSPI.h>
#include <SPI.h>

TFT_eSPI tft = TFT_eSPI();

const int SENSOR_PIN = 34;
const int BL_PIN     = 32;

const int LIM_SECO   = 800;
const int LIM_MEDIO  = 1300;
const int LIM_ALTO   = 1800;
const int ADC_MAX    = 2200;

const uint16_t COR_SECO  = TFT_RED;
const uint16_t COR_MEDIO = TFT_YELLOW;
const uint16_t COR_ALTO  = TFT_CYAN;
const uint16_t COR_MAX   = TFT_BLUE;
const uint16_t COR_BG    = TFT_BLACK;
const uint16_t COR_TEXTO = TFT_WHITE;

const int BAR_X = 30;
const int BAR_Y = 58;
const int BAR_W = 88;
const int BAR_H = 200;

int     ultimoValor  = -999;
String  ultimoStatus = "";

unsigned long ultimoMs     = 0;
unsigned long ultimoSalvo  = 0;
const unsigned long INTERVALO        = 250;
const unsigned long INTERVALO_SALVAR = 5000;

// ---------------------------------------------------------
void getStatus(int valor, String &status, uint16_t &cor) {
  if (valor < LIM_SECO) {
    status = "SECO";        cor = COR_SECO;
  } else if (valor < LIM_MEDIO) {
    status = "NIVEL MEDIO"; cor = COR_MEDIO;
  } else if (valor < LIM_ALTO) {
    status = "NIVEL ALTO";  cor = COR_ALTO;
  } else {
    status = "NIVEL MAX";   cor = COR_MAX;
  }
}

int markY(int limiar) {
  return BAR_Y + BAR_H - constrain(map(limiar, 0, ADC_MAX, 0, BAR_H), 0, BAR_H);
}

void drawBarOnly(int valor, uint16_t cor) {
  tft.fillRect(BAR_X, BAR_Y, BAR_W, BAR_H, COR_BG);
  int fill = constrain(map(valor, 0, ADC_MAX, 0, BAR_H), 0, BAR_H);
  tft.fillRect(BAR_X, BAR_Y + (BAR_H - fill), BAR_W, fill, cor);
  tft.drawFastHLine(BAR_X - 4, markY(LIM_SECO),  BAR_W + 8, COR_SECO);
  tft.drawFastHLine(BAR_X - 4, markY(LIM_MEDIO), BAR_W + 8, COR_MEDIO);
  tft.drawFastHLine(BAR_X - 4, markY(LIM_ALTO),  BAR_W + 8, COR_ALTO);
}

void drawADC(int valor) {
  tft.fillRect(0, 32, tft.width(), 20, COR_BG);
  tft.setTextFont(2);
  tft.setTextColor(TFT_DARKGREY, COR_BG);
  tft.setCursor(4, 34);
  tft.print("ADC: ");
  tft.setTextColor(COR_TEXTO, COR_BG);
  tft.print(valor);
}

void drawStatus(const String &status, uint16_t cor) {
  tft.fillRect(0, 266, tft.width(), 54, COR_BG);
  tft.setTextFont(2);
  tft.setTextColor(cor, COR_BG);
  int tw = tft.textWidth(status);
  tft.setCursor((tft.width() - tw) / 2, 274);
  tft.print(status);
}

void drawTelaCompleta(int valor, const String &status, uint16_t cor) {
  tft.fillScreen(COR_BG);

  tft.setTextFont(2);
  tft.setTextColor(COR_TEXTO, COR_BG);
  int tw = tft.textWidth("Sensor de Agua");
  tft.setCursor((tft.width() - tw) / 2, 7);
  tft.print("Sensor de Agua");

  tft.drawFastHLine(0, 27, tft.width(), TFT_DARKGREY);
  drawADC(valor);
  tft.drawFastHLine(0, 54, tft.width(), TFT_DARKGREY);
  tft.drawRect(BAR_X - 1, BAR_Y - 1, BAR_W + 2, BAR_H + 2, TFT_DARKGREY);
  drawBarOnly(valor, cor);

  int lx = BAR_X + BAR_W + 7;
  tft.setTextFont(1);
  tft.setTextColor(TFT_DARKGREY, COR_BG);
  tft.setCursor(lx, BAR_Y + 1);            tft.print("MAX");
  tft.setCursor(lx, markY(LIM_ALTO)  - 4); tft.print("ALT");
  tft.setCursor(lx, markY(LIM_MEDIO) - 4); tft.print("MED");
  tft.setCursor(lx, markY(LIM_SECO)  - 4); tft.print("SEC");

  tft.drawFastHLine(0, 263, tft.width(), TFT_DARKGREY);
  drawStatus(status, cor);
}

// ---------------------------------------------------------
void setup() {
  Serial.begin(115200);

  // Cabeçalho do arquivo — aparece uma vez ao ligar
  Serial.println("segundos,adc,status");

  pinMode(BL_PIN, OUTPUT);
  digitalWrite(BL_PIN, HIGH);

  tft.init();
  tft.setRotation(0);
  tft.fillScreen(COR_BG);

  tft.setTextFont(2);
  tft.setTextColor(TFT_GREEN, COR_BG);
  int tw = tft.textWidth("Iniciando...");
  tft.setCursor((tft.width() - tw) / 2, 148);
  tft.print("Iniciando...");
  delay(800);
}

void loop() {
  unsigned long agora = millis();
  if (agora - ultimoMs < INTERVALO) return;
  ultimoMs = agora;

  long soma = 0;
  for (int i = 0; i < 4; i++) soma += analogRead(SENSOR_PIN);
  int valor = soma / 4;

  String status;
  uint16_t cor;
  getStatus(valor, status, cor);

  if (status != ultimoStatus) {
    drawTelaCompleta(valor, status, cor);
  } else if (abs(valor - ultimoValor) > 8) {
    drawADC(valor);
    drawBarOnly(valor, cor);
  }

  ultimoStatus = status;
  ultimoValor  = valor;

  // Imprime linha CSV limpa a cada 5 segundos
  if (agora - ultimoSalvo >= INTERVALO_SALVAR) {
    ultimoSalvo = agora;
    Serial.printf("%lu,%d,%s\n", agora / 1000, valor, status.c_str());
  }
}
