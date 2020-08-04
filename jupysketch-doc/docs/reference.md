## Line
### Yaml
```yaml
A: point(-5,-5)
B: point(5,5)
line: Line(A,B)
```
### Python
```python
A = point(-5,-5)
B = point(5,5)
line = Line(A,B)
```
![line](reference/line.svg)
## Rectangle
### Yaml
```yaml
L: 8
h: 5
p: point(-(L/2),-(h/2))
rectangle: Rectangle(p,L,h)
```
### Python
```python
L = 8
h = 5
p = point(-(L/2),-(h/2))
rectangle = Rectangle(p,L,h)
```
![rectangle](reference/rectangle.svg)
## Circle
### Yaml
```yaml
circle: Circle(point(0,0),5)
```
### Python
```python
circle = Circle(point(0,0),5)
```
![circle](reference/circle.svg)
## Triangle
### Yaml
```yaml
L: 3.0
W: 4.0
triangle: Triangle(p1=(W/2,0), p2=(3*W/2,W/2), p3=(4*W/5.,L))
```
### Python
```python
L = 3.0
W = 4.0
triangle = Triangle(p1=(W/2,0), p2=(3*W/2,W/2), p3=(4*W/5.,L))
```
![triangle](reference/triangle.svg)
## Distance with text
### Yaml
```yaml
fontsize: 14
t: r'$ 2\pi R^2 $'  # sample text
dwt: Distance_wText((-4,0), (8, 5), t, fontsize)
```
### Python
```python
fontsize=14
t = r'$ 2\pi R^2 $'  # sample text
dwt = Distance_wText((-4,0), (8, 5), t, fontsize)
```
![Distance with text](reference/distancewithtext.svg)
## Text
### Yaml
```yaml
text: Text(r'$c$', point(0,0))
```
### Python
```python
text = Text(r'$c$', point(0,0))
```
![Text](reference/text.svg)
## Cross (self designed)
### Yaml
```yaml
c: point(0,0)
l: 0.1
line1: Line(c+point(-l,l),c+point(l,-l))
line2: Line(c+point(l,l), c+point(-l,-l))
cross: 
    formula: "Composition({'line1': line1, 'line2': line2})"
    style:
        linecolor: black
        linewidth: 1
```
### Python
```python
c = point(0,0)
l = 0.1
line1 = Line(c+point(-l,l),c+point(l,-l))
line2 = Line(c+point(l,l), c+point(-l,-l))
cross = Composition({'line1': line1, 'line2': line2})
cross.set_linecolor('black')
cross.set_linewidth(1)
```
![Cross](reference/cross.svg)

## Cross (from shapes)
### Yaml
```yaml
cross1: Cross(point(0,0))
```
### Python
```python
cross = Cross(point(1,0))
```
![Cross](reference/cross.svg)

## Code initialization

Using the following framework in a jupyter notebook

```python
[1]: %matplotlib widget
[2]: from pysketcher import *
[3]: drawing_tool.set_coordinate_system(xmin=-10, xmax=10,ymin=-10, ymax=10,axis=True)
[4]: drawing_tool.mpl.gcf().canvas
```
for Yaml, you need the added steps

```python
head = """\
libraries: ["from math import tan, radians, sin, cos","from pysketcher import *"]
"""
myfig={}
sketchParse(head,myfig)
```

### Yaml

```python
myfig={}
sketch="""
# put here the yaml 'object' definition
"""
drawing_tool.erase()
sketchParse(sketch,myfig)
# replace 'object' by the actual one
d = myfig['object'].draw() 
drawing_tool.display()
```

### Python

```python
drawing_tool.erase()
# put the code of the object case here
# replace object by the actual name line, rectangle, circle...
object.draw()
drawing_tool.display()
```