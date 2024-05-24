
// we want to start this using a python script
// recast last two parts of command to integers so that they are centered frequency and pulse width respectively
// how to calculate time in microseconds from frequency in Hz



//TTL Emulator for the CMS project
//Used on an Arduino Mega 2560
int pulseWidth = 1;
int timeLow;

int lowRNG = 5; // lower bound of time between pulses
int upRNG = 10; // upper bound of time between pulses

int outPin = 13; // Setup pin LED L as test output
int freq;
bool go = false;
bool clk = false;
bool ran = false;

void setup() {
  // start serial at baud rate of 9600
  Serial.begin(9600);
  Serial.println("Send 'start' over the serial bus to begin. Send 'stop' to stop signal.");
  
  pinMode(outPin, OUTPUT);
  
  // use analog pin as random seed so that numbers are more randomized
  randomSeed(analogRead(0));
}

void loop() {
  //Wait for serial to be avalible on the board
  if (Serial.available() > 0){
    String command = Serial.readString();
    command.trim();

    // if the command is stop we stop
    if (command == "stop"){
      go = false;
    }
    else{
      // if the command is not stop it must have 3 parts: "start,[type],[pulseWidth],[Frequency]"
      // check if our command string follows this format
      int delim1 = command.indexOf(",");
      int delim2 = command.indexOf(",", delim1 +1);
      int delim3 = command.indexOf(",", delim2 +1);
      String cmdSub0 = command.substring(0,5); // first substring must be start
      String cmdSub1 = command.substring(delim1+1, delim2);
      String cmdSub2 = command.substring(delim2+1, delim3);
      String cmdSub3 = command.substring(delim3+1,command.length()+1);
  
      Serial.println(cmdSub0);
      Serial.println(cmdSub1);
      Serial.println(cmdSub2);
      Serial.println(cmdSub3);
  
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
        pulseWidth = cmdSub2.toInt();
        freq = cmdSub3.toInt();
      }
      else{
        Serial.println("make sure that the second two arguments are numeric");
        go = false;
      }

      
      // check centered frequency
      // check pulse length in microseconds?

    }
    
  }
}

  if(go && ran == true){
    // put lowtime between lower and upper bounds in microseconds
    timeLow = random(lowRNG,upRNG + 1);
    Serial.println(timeLow);
    delayMicroseconds(timeLow);
    
    // This is in place of triggering signal
    digitalWrite(13,HIGH);
    delayMicroseconds(pulseWidth);
    digitalWrite(13,LOW);
  }
  if(go && clk == true){
    //CHANGE THIS LATER
    Serial.println(timeLow);
    delayMicroseconds(timeLow);
    digitalWrite(13,HIGH);
    delayMicroseconds(pulseWidth);
    digitalWrite(13,LOW);
  }
}
