#include <math.h>
//TTL Emulator for the CMS project
//Used on an Arduino Mega 2560

int pulseWidth = 1; // amount of time (in microseconds) that signal is high
int freq; // desired frequency for clocked mode or approximate centered frequency for random mode
long timeLow; // long becuase int is not always large enough for numbers used
int outPin = 12; // pin with output signal
int reject = 20; // threshold, in microseconds for rejecting randomly generated times between pulses
bool go = false; // true = signal on, false = signal off
bool clk = false; // clocked trigger mode on when true
bool ran = false; // random trigger mode on when true

void setup() {
  // set up serial interface
  Serial.begin(9600);
  Serial.println("Send 'start' over the serial bus to begin. Send 'stop' to stop signal.");
  pinMode(outPin, OUTPUT);
  // use analog pin as random seed so that numbers are more randomized
  randomSeed(analogRead(0));
}


void loop() {
  // read serial if available
  if (Serial.available() > 0){
    String command = Serial.readString();
    command.trim();

    // if the command is stop we stop
    if (command == "stop"){
      go = false;
    }

    // if the command is not stop it must have 4 parts: "start,[type],[pulseWidth],[Frequency]"
    else{
      // check if our command string follows this format
      int delim1 = command.indexOf(",");
      int delim2 = command.indexOf(",", delim1 +1);
      int delim3 = command.indexOf(",", delim2 +1);
      String cmdSub0 = command.substring(0,5); // first substring must be start
      String cmdSub1 = command.substring(delim1+1, delim2);
      String cmdSub2 = command.substring(delim2+1, delim3);
      String cmdSub3 = command.substring(delim3+1,command.length()+1);
  
      //Serial.println(cmdSub0);
      //Serial.println(cmdSub1);
      //Serial.println(cmdSub2);
      //Serial.println(cmdSub3);
  
      // check whether to start
      if (cmdSub0 == "start"){
        go = true;
        cmdSub0 = "";
        
        // check clocked or random trigger mode
        if (cmdSub1 == "clk"){
          clk = true;
          ran = false;
          cmdSub1 = "";
        }
        else if (cmdSub1 == "rand"){
          clk = false;
          ran = true;
          cmdSub1 = "";
        }
        else{
          Serial.println("there was an issue with your command");
        }

      // check that numeric values are numeric  
      bool pwIsNum = true;
      for (int i = 0; i < cmdSub2.length(); i++){
        if (not isDigit(cmdSub2.charAt(i))){
          pwIsNum = false;
        }
      }
      bool freqIsNum = true;
      for (int i = 0; i < cmdSub3.length(); i++){
        if (not isDigit(cmdSub3.charAt(i))){
          freqIsNum = false;
          }    
      }

      if(pwIsNum==true && freqIsNum==true){
        //Serial.println("Both are Numbers");
        pulseWidth = cmdSub2.toInt();
        freq = cmdSub3.toInt();        
        float tempTime = (1/float(freq)) * 1000000 - pulseWidth;
        timeLow = long(round(tempTime));
        Serial.println("freq");
        Serial.println(freq);
        Serial.println("timeLow");
        Serial.println(timeLow);
        //Serial.println("tempTime");
        //Serial.println(tempTime);
        //Serial.println("pulseWidth");
        //Serial.println(pulseWidth);
        //Serial.println("timelow");
        //Serial.println(timeLow);
      }
      else{
        Serial.println("make sure that the second two arguments are numeric");
        go = false;
      }

    }
    
  }
}

  
  // clocked trigger mode

  // delayMicroseconds is only accurate for values up to 16383
  if(go && clk == true && timeLow < 16383){
    //Serial.println(timeLow);
    delayMicroseconds(timeLow);
    digitalWrite(outPin,HIGH);
    delayMicroseconds(pulseWidth);
    digitalWrite(outPin,LOW);
  }
  // if our delay time is greater than or equal to 16383, convert to milliseconds and use standard delay
  else if(go && clk == true && timeLow >= 16383){
    //Serial.println(timeLow);
    delay(int(timeLow/1000));
    digitalWrite(outPin,HIGH);
    delayMicroseconds(pulseWidth);
    digitalWrite(outPin,LOW);
  }
  

  // random trigger mode
  else if(go && ran == true){
    float t = float(random(0,1000000)) / 1000000.0; // generate random t between 0 and 1
    long ranTimeLow = -1.0 / float(freq) * log(t) * 1000000; // multiply by 1000000 so that expression is in microseconds
    if (ranTimeLow >= reject){
      //Serial.println(ranTimeLow);
      delayMicroseconds(ranTimeLow);
      // triggering signal
      digitalWrite(outPin,HIGH);
      delayMicroseconds(pulseWidth);
      digitalWrite(outPin,LOW);
      }
    }
}