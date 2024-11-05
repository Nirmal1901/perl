use strict;
use warnings;
use Car;

my $car = Car->new(brand => "Toyota", model => "Corolla");

print "Brand: ", $car->get_brand(), "\n";
print "Model: ", $car->get_model(), "\n";

$car->set_brand("Honda");
$car->set_model("Civic");

print "Updated Brand: ", $car->get_brand(), "\n";
print "Updated Model: ", $car->get_model(), "\n";
