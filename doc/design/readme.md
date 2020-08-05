# Design Notes

# Alternatives Drawing Libraries
   
   Instead of Matplotlib, the following libraries could be used
   
   - Casey Duckering [drawSvg](https://github.com/cduck/drawSvg)
   - Martin Renou [ipycanvas](https://github.com/martinRenou/ipycanvas)

# Parsing yaml files expressions

   In a point of time, we need to verify the syntax of yaml sketch definition, here are some parser which might help
   
   - Paul McGuire [pyparsing](https://github.com/pyparsing/pyparsing)

   in fact this is solved (an now implemented this summer 8/5/2020) with the ast module
   see the function sketchParse in the shapes.py module