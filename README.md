# TTL-Emulator

This is a Transistor-Transistor Logic trigger that was developed for CMS at CERN. The Arduino code has two modes: One is a stable clock at a desired frequency and pulse width. The second is a pseudo random clock with a centralized frequency and consistant pulse rate. Both will output a 3.3V pulse, because Arduino pins do that when set to HIGH.