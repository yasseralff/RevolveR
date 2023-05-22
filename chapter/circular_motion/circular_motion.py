import re
import sympy

'''
UML Class Diagram

     +------------------------------+
     |            Formula           |
     +------------------------------+
     | - v : sympy.symbols('v')     |
     | - r : sympy.symbols('r')     |
     | - m : sympy.symbols('m')     |
     | - ca : sympy.symbols('ac')   |
     | - f : sympy.symbols('f')     |
     | - eqca : sympy.Eq            |
     | - eqf : sympy.Eq             |
     | - centripetal_acceleration() |
     | - force()                    |
     | - velocity()                 |
     | - mass()                     |
     | - radius()                   |
     +------------------------------+

                ^
                |
                |
                |

+----------------------------------------------+
|                CircularMotion                |
+----------------------------------------------+
| - formula : Formula                          |
| - circular_keywords: list                    |
| - force_keywords: list                       |
| - problem_type(problem_statement: str) : str |
| - getCircular(problem_statement: str) : str  |
| - getForces(problem_statement: str) : str    |
+----------------------------------------------+
'''


class Formula:
    def __init__(self):
        self.v = sympy.symbols('v')     # velocity
        self.r = sympy.symbols('r')     # radius
        self.m = sympy.symbols('m')     # mass
        self.ca = sympy.symbols('ac')   # centripetal acceleration
        self.f = sympy.symbols('f')     # force

    def centripetal_acceleration(self):
        self.eqca = sympy.Eq(self.ca, self.v ** 2 / self.r)
        self.eqf = sympy.Eq(self.f, self.m * self.ca)
        self.ca = sympy.solve(self.eqca, self.ca)[0]

    def force(self):
        self.eqca = sympy.Eq(self.ca, self.v ** 2 / self.r)
        self.eqf = sympy.Eq(self.f, self.m * self.ca)
        self.f = sympy.solve(self.eqf, self.f)[0]

    def velocity(self):
        self.eqca = sympy.Eq(self.ca, self.v ** 2 / self.r)
        self.eqf = sympy.Eq(self.f, self.m * self.ca)
        self.v = sympy.solve(self.eqca, self.v)[0]

    def mass(self):
        self.eqca = sympy.Eq(self.ca, self.v ** 2 / self.r)
        self.eqf = sympy.Eq(self.f, self.m * self.ca)
        self.m = sympy.solve(self.eqca, self.v)[0]

    def radius(self):
        self.eqca = sympy.Eq(self.ca, self.v ** 2 / self.r)
        self.eqf = sympy.Eq(self.f, self.m * self.ca)
        self.r = sympy.solve(self.eqca, self.v)[0]


class CircularMotion:
    def __init__(self, circular_keywords, force_keywords):
        self.formula = Formula()
        self.circular_keywords = circular_keywords
        self.force_keywords = force_keywords

    def problem_type(self, problem_statement):
        problem_type = None

        # Check for circular-related problems
        for keyword in self.circular_keywords:
            if re.search(keyword, problem_statement, re.IGNORECASE):
                problem_type = 'circular'
                break

        # Check for force-related problems
        if not problem_type:
            for keyword in self.force_keywords:
                if re.search(keyword, problem_statement, re.IGNORECASE):
                    problem_type = 'forces'
                    break

        return problem_type

    def getCircular(self, problem_statement):
        # Extract variables from the problem statement
        radius_regex = r'radius\s*of\s*([\w\.]+)\s*(\w+)'
        velocity_regex = r'speed\s*of\s*([\w\.]+)\s*(\w+)'

        # Extract numeric values and units
        radius_match = re.search(radius_regex, problem_statement, re.IGNORECASE)
        if radius_match:
            radius = radius_match.group(1)
            radius_unit = radius_match.group(2)
            if radius.isnumeric():
                self.formula.r = float(radius)
            else:
                self.formula.r = sympy.symbols(radius)

            # Check units and convert if necessary
            if radius_unit == 'cm':
                self.formula.r /= 100
            elif radius_unit == 'mm':
                self.formula.r /= 1000
            elif radius_unit == 'ft':
                self.formula.r *= 0.3048
            elif radius_unit == 'yd':
                self.formula.r *= 0.9144

        velocity_match = re.search(velocity_regex, problem_statement, re.IGNORECASE)
        if velocity_match:
            velocity = velocity_match.group(1)
            velocity_unit = velocity_match.group(2)
            if velocity.isnumeric():
                self.formula.v = float(velocity)
            else:
                self.formula.v = sympy.symbols(velocity)

            # Check units and convert if necessary
            if velocity_unit == 'rpm':
                self.formula.r *= sympy.pi / 30
            elif velocity_unit in ('rad', 'rad/s', 'radian'):
                self.formula.v *= self.formula.r

        # Calculate and return the solution
        self.formula.centripetal_acceleration()
        try:
            return f"The centripetal acceleration is {format(float(self.formula.ca), '.3f')} m/s^2."
        except TypeError:
            return f"The centripetal acceleration is {self.formula.ca} m/s^2."

    def getForces(self, problem_statement):
        # Extract variables from the problem statement
        radius_regex = r'radius\s*of\s*([\w\.]+)\s*(\w+)'
        velocity_regex = r'speed\s*of\s*([\w\.]+)\s*(\w+)'
        mass_regex = r'mass\s*of\s*([\w\.]+)\s*(\w+)'
        acceleration_regex = r'acceleration\s*of\s*([\w\.]+)\s*(\w+)'

        radius_match = re.search(radius_regex, problem_statement, re.IGNORECASE)
        if radius_match:
            radius = radius_match.group(1)
            radius_unit = radius_match.group(2)
            if radius.isnumeric():
                self.formula.r = float(radius)
            else:
                self.formula.r = sympy.symbols(radius)

            # Check units and convert if necessary
            if radius_unit == 'cm':
                self.formula.r /= 100
            elif radius_unit == 'mm':
                self.formula.r /= 1000
            elif radius_unit == 'ft':
                self.formula.r *= 0.3048
            elif radius_unit == 'yd':
                self.formula.r *= 0.9144

        velocity_match = re.search(velocity_regex, problem_statement, re.IGNORECASE)
        if velocity_match:
            velocity = velocity_match.group(1)
            velocity_unit = velocity_match.group(2)
            if velocity.isnumeric():
                self.formula.v = float(velocity)
            else:
                self.formula.v = sympy.symbols(velocity)

            # Check units and convert if necessary
            if velocity_unit == 'rpm':
                self.formula.r *= sympy.pi / 30
            elif velocity_unit in ('rad', 'rad/s', 'radian'):
                self.formula.v *= self.formula.r

        mass_match = re.search(mass_regex, problem_statement, re.IGNORECASE)
        if mass_match:
            mass = mass_match.group(1)
            mass_unit = mass_match.group(2)
            if mass.isdigit():
                self.formula.m = float(mass)
            else:
                try:
                    self.formula.m = float(mass)
                except ValueError:
                    self.formula.m = sympy.symbols(mass)

            if mass_unit == 'gram' or mass_unit == 'g':
                self.formula.m *= 1000

        acceleration_match = re.search(acceleration_regex, problem_statement, re.IGNORECASE)
        if acceleration_match:
            acceleration = acceleration_match.group(1)
            acceleration_unit = acceleration_match.group(2)
            if acceleration.isnumeric():
                self.formula.ca = float(acceleration)
            else:
                self.formula.ca = sympy.symbols(acceleration)

            if acceleration_unit == 'm':
                self.formula.ca /= self.formula.r

            self.formula.force()

        else:
            self.formula.centripetal_acceleration()
            self.formula.force()

        # Calculate and return the solution
        try:
            return f"The force is {format(float(self.formula.f), '.3f')} N."
        except TypeError:
            return f"The force is {self.formula.f} N."

    def solve_physics_problem(self, problem_statement):
        problem_type = self.problem_type(problem_statement)
        # Solve the problem based on its type
        if problem_type == 'circular':
            return self.getCircular(problem_statement)

        elif problem_type == 'forces':
            # Implement forces and Newton's laws problem solver
            return self.getForces(problem_statement)

        else:
            return "Error: Problem type not recognized"

# am = CircularMotion()
# solution = am.solve_physics_problem(problem_statement)
# print(solution)
# print(am.problem_type(problem_statement))
