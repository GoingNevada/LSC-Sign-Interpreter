#include <BluetoothSerial.h>

BluetoothSerial BT;

// ASIGNACION DE PINES
const int pulgar = 36; // ADC1_4 GPIO36
const int indice = 39; // ADC1_7 GPIO39
const int corazon = 34; // ADC1_6 GPIO34
const int anular = 35; // ADC1_3 GPIO35
const int menique = 32; // ADC1_0 GPIO32
int dif[5];
int lecturafin[5]={0,0,0,0,0};

void setup()
{
  Serial.begin(115200);
  BT.begin("SACAMO_ESP32");
  pinMode(2, OUTPUT);
}

void loop()
{
  if (BT.available()>0){
    char datos = BT.read();
    if (datos == '1')
    {
      digitalWrite(2, HIGH);
    }
    if (datos == '0'){
      digitalWrite(2,LOW);
    }
  }
         // lecturas:   0 -> pulgar,       1 -> indice,       2 -> corazon,       3 -> anular,        4 -> menique
  int lecturaini[5]={analogRead(pulgar),analogRead(indice),analogRead(corazon),analogRead(anular),analogRead(menique)};
  if (lecturafin[0]!=0){
    for (int i=0; i<5; i++){
      dif[i] = lecturaini[i]-lecturafin[i];
      if (abs(dif[i]) > 50)
      {
        lecturafin[i]=lecturaini[i];
      }
      else{
        lecturafin[i]=lecturafin[i];
      }
      BT.print(lecturafin[i]);
      if (i<4){ BT.print(",");}
    }
  }
  else{
    for (int i=0; i<5; i++){
      lecturafin[i]=lecturaini[i];
      BT.print(lecturafin[i]);
      if (i<4){ BT.print(",");}
    }
  }
  BT.print("\n");
  delay(100);
}
