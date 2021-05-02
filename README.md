# Fractal-gen
Fractal-gen is a open library which can be used to generate, experiment and create fractal images using IFSs. IFSs are Iterated Function Systems which are used in one of the methods in constructing fractals. IFSs are simply set of Affine equations upon which we apply different algorithms to generate fractal images. For further more detailed explanation on IFSs and their workings we recommend users to go through these links below:
1. http://paulbourke.net/fractals/ifs/
2. https://larryriddle.agnesscott.org/ifs/ifs.htm
3. https://www.sciencedirect.com/book/9780120790616/fractals-everywhere

 Out of many algorithms which generate fractals, our library generates fractals based on Deterministic and Random Iteration algorithms. 
 
 There are many ways of describing the affine transformations for iterated functions systems (IFS) which are as follows:

1. x = r cos(θ) x + s sin(θ) y + h <br />
 y = -r sin(θ) x + s cos(θ) y + k<br />

and <br />

2. xn+1 = a xn + b yn + c<br />
 yn+1 = d xn + e yn + f<br />

and <br />

<img src="https://github.com/Navaneethnanda/fractal-gen/blob/main/imgs/CodeCogsEqn.svg" height=400 width=400 />

Out of all the most used notation is the third one. Many IFSs are available in similar format to the 3 notation or they can be derived from different forms to the 3rd one some of mostly used notations are below

![Capture](https://user-images.githubusercontent.com/37890718/114451965-84120b80-9bf5-11eb-92a8-e04e05b84c99.PNG)


Deterministic:
![Capture1](https://user-images.githubusercontent.com/37890718/114452267-e2d78500-9bf5-11eb-85c0-24fd4b97fbd1.PNG)

random iteration:
![Capture2](https://user-images.githubusercontent.com/37890718/114452284-e834cf80-9bf5-11eb-90db-368157db850d.PNG)

So all the details we need to generate fractal image are values of a,b,c,d,e,f of an affine traformation in a IFS while using deterministic algorithm and probabilities in addition while using random iteration algorithm. We recommend users to get a good picture on working of IFSs and representations of IFSs before continuing further.
```

# How to use 
First initialize IFS object and pass IFSs Through AddEquations method like shown below:

    object = IFS()
    eqns=[[a1,b1,c1,d1,e1,f1],
    [a2,b2,c2,d2,e2,f2],
    .
    .
    [an,bn,cn,dn,en,fn]]
    #probabilities should be added if your intent is to use random iteration algorithm [[a1,b1,c1,d1,e1,f1,p1],[a2,b2,c2,d2,e2,f2,p2],...     [an,bn,cn,dn,en,fn,pn]].
    object.AddEquations(eqns)
    
    
bro ikkada nundi pandas lo code examples and output format mention chey vro just pai paina inka paina matrix pettu ra nku raale try chesa lready

