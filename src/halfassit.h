#ifndef HALFASS_H
#define HALFASS_H

#include <godot_cpp/classes/sprite2d.hpp>

namespace godot {

class HalfAssIT: public Sprite2D {
	GDCLASS(HalfAssIT, Sprite2D)

private:
	double time_passed;
	double time_emit;
  double amplitude;
  double speed;

protected:
	static void _bind_methods();

public:
	HalfAssIT();
	~HalfAssIT();

public:
	void set_amplitude(const double p_amplitude);
	double get_amplitude() const;
  void _process(double delta) override;
	void set_speed(const double p_speed);
	double get_speed() const;
};
}

#endif