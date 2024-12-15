package Car;
use strict;
use warnings;

sub new {
    my ($class, %args) = @_;
    my $self = {
        brand => $args{brand} || "Unknown",
        model => $args{model} || "Unknown",
    };
    bless $self, $class;
    return $self;
}

sub set_brand {
    my ($self, $brand) = @_;
    $self->{brand} = $brand;
}

sub get_brand {
    my $self = shift;
    return $self->{brand};
}

sub set_model {
    my ($self, $model) = @_;
    $self->{model} = $model;
}

sub get_model {
    my $self = shift;
    return $self->{model};
}

1;
