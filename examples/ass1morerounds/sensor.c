#include "sensor.h"
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define PI 3.1415926535
// Get a random value between min and max
float random_value(float min, float max) {
float scale = rand() / (float) RAND_MAX;
return min + scale * (max - min);
}
// Implementation of Box Muller_transform to generate gaussian distribution
// "mu" is mean, "segma^2" is variance
float gaussian(double mu, double sigma)
{
double epsilon = 0.00001;
// Generate two random numbers and make sure that the first one is greater

double u1, u2;
do
{
u1 = random_value(0,1);
u2 = random_value(0,1);
}
while (u1 <= epsilon);
//compute z0 and z1 by applying the Box-Muller formula
double mag = sigma * sqrt(-2.0 * log(u1));
double z0 = mag * cos(2*PI * u2) + mu;
double z1 = mag * sin(2*PI * u2) + mu;
// return only one value of them
return random_value(0,1)>0.5? z0:z1;
}
// Read temperature from sensor
float read_temperature(float additive_noise, float amplification_factor, float
fading_factor) {
float temperature = 25.0;
temperature = (temperature + additive_noise) * amplification_factor *
fading_factor;
return temperature;
}
// Read humidity from sensor
float read_humidity(float additive_noise, float amplification_factor, float
fading_factor) {
float humidity = 40.0;
humidity = (humidity + additive_noise) * amplification_factor *
fading_factor;
return humidity;
}
// Read pressure from sensor
float read_pressure(float additive_noise, float amplification_factor, float
fading_factor) {
float pressure = 101.0 * 1000;
pressure = (pressure + additive_noise) * amplification_factor *
fading_factor;
return pressure;
}
// Get additive noise for readed value
float get_additive_noise() {
return gaussian(0, 1);
}
// Get amplification factor for sensor
float get_amplification_factor() {
return 2.1;
}
// Get fading factor for transmitting process
float get_fading_factor() {
return 0.5;
}
