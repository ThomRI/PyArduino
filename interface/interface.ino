/* Commands */
  #define DONE 100

  #define PIN_MODE 101
  #define DIGITAL_WRITE 102
  #define DIGITAL_READ 103
  #define ANALOG_WRITE 104
  #define ANALOG_READ 105


void setup() {
  Serial.begin(115200);
  Serial.flush(); // Flushes the Serial buffer
  
  /* Initializing communication */
  Serial.write((char) 0);
  Serial.write((char) 255);
  Serial.write((char) 0);
}

void loop() {
  char command = 0;
  if(Serial.available() > 0) { // Blocks the loop while no PC instruction is detected
    command = Serial.read();
    
    switch(command) {
      case PIN_MODE:      cmd_pinMode();      break;
      case DIGITAL_WRITE: cmd_digitalWrite(); break;
      case DIGITAL_READ:  cmd_digitalRead();  break;
      case ANALOG_WRITE:  cmd_analogWrite();  break;
      case ANALOG_READ:   cmd_analogRead();   break;

      default: 
        Serial.print("Unknown command : "); 
        Serial.print(command); 
        Serial.print("\n");
    }
  }

}

void wait_args(unsigned int nbr = 1) {
  while(Serial.available() < nbr);
}

void done() {
  Serial.write(DONE);
}

/* Arduino syntax : pinMode(pin, mode) */
void cmd_pinMode() {
  char pin = 0, mode = 0;
  wait_args(2);

  pin = Serial.read();
  mode = Serial.read();

  pinMode(pin, mode);
  done();
}

/* Arduino syntax : digitalWrite(pin, value) */
void cmd_digitalWrite() {
  char pin = 0, value = 0;
  wait_args(2);

  pin = Serial.read();
  value = Serial.read();

  digitalWrite(pin, value);
  done();
}

/* Arduino syntax : digitalRead(pin) */
void cmd_digitalRead() {
  char pin = 0;
  wait_args(1);

  pin = Serial.read();
  digitalRead(pin);

  Serial.write( digitalRead(pin) );
}

/* Arduino syntax : analogWrite(pin, value) */
void cmd_analogWrite() {
  char pin = 0, value = 0;
  wait_args(2);

  pin = Serial.read();
  value = Serial.read();

  analogWrite(pin, value);
  done();
}

/* Arduino syntax : analogRead(pin) */
void cmd_analogRead() {
   char pin = 0;
   wait_args(1);

   value = analogRead(pin); // Coded on 10 bits !

   Serial.write( (value >> 8) & 0xFF ) ;  // 8 first bits (that are thus shifted 8 spots to the right before being compared to 0xFF)
   Serial.write( value & 0xFF );          // 8 last bits of the value
}
