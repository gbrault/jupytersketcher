## A language to describe a sketch

Pysketcher initial version [HPL Pysketcher]() enable sketch definition in python. HPL is showing the hierachical nature of sketches. This is implemented via the Composition function. One can further grasp this using the graphviz_dot function applied to discover the composition herarchy implemented as a graphviz image [see The hierarchy of the "friction" main object](#the-hierarchy-of-the-friction-main-object) at the end of this page.

Due to the hierarchical nature of sketches, it is quite straightforward to think about using yaml as the syntax for defining a sketch.

The benefits are as follow:

* A leaner presentation of the sketch as only the data making sense is going to be used
* A more straightforward reading of the composition hierachy
* A more robust sketch definition as only a set of rules will be applied to define a sketch and no further python idiom will be intermingled

## Example

This example provides the yaml content to define the Dry Friction case

### The final sketch
![](images/dryfriction.png)

An inclined plan (the A-B edge) supports a blue rectangle which is pulled donward by the gravity. The plan makes an angle $\theta$. The sketch design enable the $\theta$ angle to change. The whole plan including the body can rotate arround the point B.

### The yaml definition

Sketcher language is defined as a yaml compliant file or string. The yaml file is a dictionnary of 

* functionnal objects (leaf objects, like Rectangle, Circle, Line etc or composition)
* extended with object style (line or fill colors, line stroke...)
* to which transformation are applied (translation, rotation...)

As a general rule, a new object suppose all parameters to be defined before they are used to construct it.

**For example, you can create a circle if the center and the radius have been defined earlier in the file.**

The general layout of a sketcher file is as follow:

* **Libraries, Construction Variables, Frame**
    * declaration of the libraries used by the objects further declared: at least pysketcher is mandatory
    * various global variable which encompass the "Construction" variables which define the object main physical dimensions, positions...
    * some "actions" corresponding to executable python sentences
        * One mandatory action is the setting of the drawing frame (drawing_tool.set_coordinate_system): it must be declared before any other pysketcher object is used.
        * Other use case of action is the setting of global parameters like default line color: (drawing_tool.set_linecolor('black')) for example
* **Objects**
    * Usually starting with the declaration of leaf simple objects
    * then aggregated using the composition object
    * Composition can be made of composition object
    * grouping leafs and composition will be further used to apply transformation latter on (based on the "physics")
    * The example presents three group of objects
        * The body object
        * The plan object
        * The friction main object
    * The plan includes the body
    * The friction includes the plan (that will be able to rotate as a group) and the ground (will stay fixed)

#### Libraries, Construction Variables, Frame
```yaml
libraries: ["from math import tan, radians, sin, cos",
            "from pysketcher import *"]
fontsize: 18
g: 9.81              # constant gravity
theta: 30.0          # inclined plane angle
L: 10.0              # sketch sizing parameter
a: 1.0               #
xmin: 0.0            # sketech min Abscissa
ymin: -3.0           # sketech min Ordinate     
rl: 2.0              # rectangle width
rL: 1.0              # rectangle length
setframe:            # sketch setup
    action: "drawing_tool.set_coordinate_system(xmin=xmin-L/5, xmax=xmin+1.5*L,ymin=ymin, ymax=ymin+1.5*L,instruction_file='tmp_mpl_friction.py')"
setblackline:        # default frame values and actions
    action: "drawing_tool.set_linecolor('black')"
B: point(a+L,0)                      # wall right end
A: point(a,tan(radians(theta))*L)    # wall left end
normal_vec: point(sin(radians(theta)),cos(radians(theta)))     # Vector normal to wall
tangent_vec: point(cos(radians(theta)),-sin(radians(theta)))   # Vector tangent to wall
help_line: Line(A,B)                 # wall line
x: a + 3*L/10.
y: help_line(x=x)    
contact: point(x, y)    
c: contact + rL/2*normal_vec
```
#### The body object
```yaml
rectangle: 
    formula: Rectangle(contact, rl, rL)
    style:
        linecolor: blue
        filled_curves: blue
    transform: ["rotate(-theta, contact)",
                "translate(-rl/2*tangent_vec)"]
N: 
    formula: Force(contact - rl*normal_vec, contact, r'$N$', text_pos='start')
    style:
        linecolor: black
mg: 
    formula: Gravity(c, rl, text='$Mg$')
    style:
        linecolor: black
wheel: 
    formula: "Composition({'outer': rectangle})"   
    style:
        shadow: 1
body: 
    formula: "Composition({'wheel': wheel, 'N': N, 'mg': mg})"
    style:
        linecolor: black
```
#### The plan object
```yaml
mB:
    formula: Text(r'$B$',B)
mA:
    formula: Text(r'$A$', A)
wall: 
    formula: Wall(x=[A[0], B[0]], y=[A[1], B[1]], thickness=-0.25,transparent=False)
    style:
        linecolor: black    
angle: 
    formula: "Arc_wText(r'$<bslash>theta$', center=B, radius=3, start_angle=180-theta, arc_angle=theta, fontsize=fontsize)"
    style:
        linecolor: black
        linewidth: 1
ground: 
     formula: Line((B[0]-L/10., 0), (B[0]-L/2.,0))
     stlye:
         linecolor: black
         linestyle: dashed
         linewidth: 1
x_const: 
    formula: Line(contact, contact + point(0,4))
    style:
        linestyle: dotted
    transform: rotate(-theta, contact)
x_axis: 
    formula: "Axis(start=contact+ 2*rl*normal_vec, length=2*rl,label='$x$', rotation_angle=-theta)"
plan: 
    formula: "Composition({'body': body, 'angle': angle, 'inclined wall': wall, 'x start': x_const, 'x axis': x_axis, 'mA': mA, 'mB': mB})"
```
#### The friction main object
```yaml

friction: 
    formula: "Composition({'plan': plan, 'ground': ground})"
```

### The hierarchy of the "friction" main object

![](images/dotfriction.png)
