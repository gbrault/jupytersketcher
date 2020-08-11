Content

* [YAML sketcher file grammar](#yaml-sketcher-file-grammar)
* [Libraries, Pysketcher Object creation, Styles, Transform](#libraries-pysketcher-object-creation-styles-transform)
* [Example](#example)
* [Code to read or write a yaml sketcher file](#code-to-read-or-write-a-yaml-sketcher-file)

## YAML sketcher file grammar

Sketcher file EBNF Grammar is

```EBNF
Sketch::= Sketch_Name Parts
Sketch_Name::= "-" " " "name: " Identifier Comment? "\n"
Parts::= "-" " " "parts:\n" Comment? Part+
Part::= Part_Name Shapes
Part_Name::= INDENT "-" " " "name: " Identifier Comment? "\n" DEDENT
Shapes::= INDENT " " " " "shapes:\n" Comment? Shape+ DEDENT
Shape::= Simple | DoAction | SketchObject
Simple::= INDENT Identifier ":" PyRightHandExpression Comment? "\n" DEDENT
DoAction::= INDENT Identifier ":" Comment? "\n" Action DEDENT
Action::= INDENT "action:" PyExpression Comment? "\n" DEDENT 
Identifier::= [A-Za-z][_A-Za-z0-9]+
Comment::= "#" STRING
```

Here is the railroad grammar diagram:

<a href="/resources/yamlpysketchergrammar.xhtml" target="_blank">Yaml Sketcher Definition</a>

<small><a href="https://bottlecaps.de/rr/ui"target="_blank">[Built thanks]</a></small>

## Libraries, Pysketcher Object creation, Styles, Transform

### Libraries

The libraries token defined in the grammar is

* a single import directive
* a list [] of import directive
* one of the import must be pysketcher!

```python
from pysketcher import *
```

### Pysketcher object creation

* The `Python pysktecher object creation` is a python class object statment. 
* The possible class are defined in this [section](/shapereference)
* Every parameter of the object creation can be an expression, based upon variables defined before in the YAML file

### Styles

The list of possible style correspond to the list of set_&lt;style> members of the corresponding pysketcher class used for the object creation. This function will be applied to the current object under creation. Parameters of this function can be variable defined upstream. 

### Transform

The transform token defined in the grammer is

* a single transform statement
* a list [] of transform statments
* a tranform statement is a transformation function that can be applied to the object under construction
* example of transform function are rotate, translate
* parameters of the transform function can be expression based upon upstream variables definition

## Example
```yaml
!!omap
- name: unknown
- parts:
  - name: head
    shapes:
      libraries: ['from math import tan, radians, sin, cos', from pysketcher import
          *]
  - name: constants
    shapes:
      fontsize: 18       # size of the characters
      g: 9.81            # constant gravity
      theta: 30.0        # inclined plane angle
      L: 10.0            # sketch sizing parameter
      a: 1.0             #
      xmin: 0.0          # sketech min Abscissa
      ymin: -3.0         # sketech min Ordinate     
      rl: 2.0            # rectangle width
      rL: 1.0            # rectangle length
  - name: frame
    shapes:
      setframe:          # sketch setup
        action: drawing_tool.set_coordinate_system(xmin=xmin-L/5, xmax=xmin+1.5*L,ymin=ymin,
          ymax=ymin+1.5*L,instruction_file='tmp_mpl_friction.py')
      setblackline:      # default frame values and actions
        action: drawing_tool.set_linecolor('black')
      B: point(a+L,0)                    # wall right end
      A: point(a,tan(radians(theta))*L)  # wall left end
      normal_vec: point(sin(radians(theta)),cos(radians(theta)))   # Vector normal to wall
      tangent_vec: point(cos(radians(theta)),-sin(radians(theta))) # Vector tangent to wall
      help_line: Line(A,B)               # wall line
      x: a + 3*L/10.                     # contact point Abscissa
      y: help_line(x=x)                  # contact point Ordinate
      contact: point(x, y)               # contact point: middle of the rectangle bottom edge
      c: contact + rL/2*normal_vec
  - name: body
    shapes:
      rectangle:
        formula: Rectangle(contact, rl, rL)
        style:
          linecolor: blue
          filled_curves: blue
        transform: ['rotate(-theta, contact)', translate(-rl/2*tangent_vec)]
      N:
        formula: Force(contact - rl*normal_vec, contact, r'$N$', text_pos='start')
        style:
          linecolor: black
      wheel:
        formula: "Composition({'outer': rectangle})"
        style:
          shadow: 1
      mc:
        formula: Text(r'$c$', c)
      body:
        formula: "Composition({'wheel': wheel, 'N': N, 'mc': mc})"
        style:
          linecolor: black
  - name: plan
    shapes:
      mB:
        formula: Text(r'$B$',B)
      mA:
        formula: Text(r'$A$', A)
      wall:
        formula: Wall(x=[A[0], B[0]], y=[A[1], B[1]], thickness=-0.25,transparent=False)
        style:
          linecolor: black
      x_const:
        formula: Line(contact, contact + point(0,4))
        style:
          linestyle: dotted
        transform: rotate(-theta, contact)
      x_axis:
        formula: Axis(start=contact+ 2*rl*normal_vec, length=2*rl,label='$x$', rotation_angle=-theta)
      plan:
        formula: "Composition({'body': body, 'inclined wall': wall, 'x start': x_const,\
          \ 'x axis': x_axis, 'mA': mA, 'mB': mB})"
  - name: friction
    shapes:
      mg:
        formula: Gravity(c, rl, text='$Mg$')
        style:
          linecolor: black
      angle:
        formula: Arc_wText(r'$<bslash>theta$', center=B, radius=3, start_angle=180-theta,
          arc_angle=theta, fontsize=fontsize)
        style:
          linecolor: black
          linewidth: 1
      ground:
        formula: Line((B[0]-L/10., 0), (B[0]-L/2.,0))
        stlye:
          linecolor: black
          linestyle: dashed
          linewidth: 1
      friction:
        formula: "Composition({'plan': plan, 'ground': ground, 'mg': mg, 'angle':\
          \ angle})"
```

## Code to read or write a yaml sketcher file

To read a YAML Pysketcher file definition:

```python
from pysketcher import *
myfig={}
sketch = Sketch(myfig)
sketch.file2Sketch("dryfriction.yml")
#...............  can now use sketch to draw something ..................
```

To write a YAML Pysketcher file definition:

```python
from pysketcher import *
myfig={}
sketch = Sketch(myfig)
#.............  need to create some Pysketcher objects in the sketch .................
sketch.file2Sketch("dryfriction.yml")
```