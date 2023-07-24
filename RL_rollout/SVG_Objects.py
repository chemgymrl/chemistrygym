import numpy as np



#simple flame

FLAME=np.array([[0.42483848, 0.85188591],[0.64150102, 0.88731502],
       [0.77067357, 0.64771108],[0.69983741, 0.5268895 ],
       [0.68177209, 0.55813645],[0.66998415, 0.58313645],
       [0.64566762, 0.60189103],[0.74915053, 0.40755091],
       [0.4088589 , 0.24856727],[0.48733714, 0.0792319 ],
       [0.33664272, 0.17853715],[0.24844822, 0.34034301],
       [0.24150273, 0.47089751],[0.17690989, 0.42019524],
       [0.18109864, 0.4320192 ],[0.14150626, 0.4125662 ],
       [0.19984132, 0.5493726 ],[0.08941687, 0.60492444],
       [0.204005  , 0.76673087],[0.27136356, 0.85136877],
       [0.38872786, 0.84576733],[0.42483611, 0.85188885]])

FLAME = (FLAME-0.5)*2

FLAME_INSTRUCT="C,,"*(FLAME.shape[0]//3)


#erlenmeyer flask oriented as if sitting on a table

ERLENMEYER=[[-0.125, -0.5],
  [-0.125, 0.0],
  [-0.5, 0.9],
  [0.07826237921249266, 0.07826237921249266, 0, 0, 0, -0.45, 1.0],
  [0.45, 1.0],
  [0.07826237921249266, 0.07826237921249266, 0, 0, 0, 0.5, 0.9],
  [0.125, 0.0],
  [0.125, -0.5]]
ERLENMEYER_INSTRUCT='LLALALLL'

#round flask with same approximate dimensions of erlenmeyer

ROUND_FLASK=[[-0.125, -0.5],
  [-0.125, 0.25],
  [0.3857217261187137, 0.3857217261187137, 0, 1, 0, 0.125, 0.25],
  [0.125, -0.5]]

ROUND_FLASK_INSTRUCT="LAL"


#ice cube

CUBE=np.array([[0.22900391, 0.13339844],
       [0.39567057, 0.09589844],
       [0.47900391, 0.07923177],
       [0.53317057, 0.07923177],
       [0.61650391, 0.10423177],
       [0.84150391, 0.16673177],
       [0.93317057, 0.20839844],
       [0.96650391, 0.27923177],
       [0.92067057, 0.4500651 ],
       [0.89150391, 0.62089844],
       [0.88317057, 0.70839844],
       [0.83317057, 0.7750651 ],
       [0.75817057, 0.8125651 ],
       [0.58733724, 0.9000651 ],
       [0.51650391, 0.9375651 ],
       [0.43317057, 0.94173177],
       [0.33317057, 0.89173177],
       [0.16650391, 0.8125651 ],
       [0.07483724, 0.77089844],
       [0.02483724, 0.70839844],
       [0.02900391, 0.60839844],
       [0.03733724, 0.38339844],
       [0.02483724, 0.27089844],
       [0.04567057, 0.19173177],
       [0.09983724, 0.15423177],
       [0.23317057, 0.13339844]])

offset=CUBE.mean(axis=0)

CUBE_INSTRUCT="LC,,"*8

CUBE_INNER=np.array([[ 0.53567052,  0.34589844],
       [ 0.31247588,  0.31109274],
       [-0.02493966,  0.29228809],
       [ 0.28567053,  0.20423271],
       [-0.01256809,  0.21909178],
       [ 0.13880174,  0.36211712],
       [ 0.48983735,  0.39173194],
       [ 0.56068106,  0.46563   ],
       [ 0.47842671,  0.68877747],
       [ 0.45233944,  0.82506555],
       [ 0.56657806,  0.70198715],
       [ 0.51977209,  0.52068466],
       [ 0.57733677,  0.40839845],
       [ 0.68414075,  0.34005966],
       [ 0.94168444,  0.37038169],
       [ 0.85650531,  0.24173386],
       [ 0.81106713,  0.32041235],
       [ 0.82121276,  0.2999327 ],
       [ 0.68983938,  0.33339463]])

CUBE_INNER_INSTRUCT="C,,"*8


CUBE-=offset
CUBE_INNER-=offset




#Depricated Beaker

BEAKER=np.array([[0.15849609, 0.21673177],
       [0.24599609, 0.22089844],
       [0.26266276, 0.81673177],
       [0.73733724, 0.81673177],
       [0.75400391, 0.22089844],
       [0.84150391, 0.21673177]])

BEAKER_WATER=np.array([[0.26266276, 0.81777344],
       [0.25432943, 0.51360677],
       [0.34182943, 0.4969401 ],
       [0.40432943, 0.52610677],
       [0.50016276, 0.4969401 ],
       [0.49983724, 0.4969401 ],
       [0.59567057, 0.52610677],
       [0.65817057, 0.4969401 ],
       [0.74567057, 0.51360677],
       [0.73733724, 0.81777344]])


#structure of c6h14

C6H14=np.array([[0.07067057, 0.5500651 ],
       [0.24150391, 0.4500651 ],
       [0.41233724, 0.5500651 ],
       [0.58733724, 0.4500651 ],
       [0.75817057, 0.5500651 ],
       [0.92900391, 0.45423177]])

C6H14_INSTRUCT="L"*6

#structure of ether

ETHER_0=np.array(
    [[0.05817057, 0.53339844],
       [0.27067057, 0.40839844],
       [0.37900391, 0.47089844],
       [0.57900391, 0.4750651 ],
       [0.69150391, 0.4125651 ],
       [0.90400391, 0.53339844]])

ETHER_0_INSTRUCT="LLMLL"

ETHER_1=[
[0.37900391, 0.47089844],
[0.44567057, 0.5125651 ],
[0.485, 0.50839844],
[0.03,0.03,0,1,1,0.48480, 0.50839844],
[0.52483724, 0.5125651 ],
[0.57900391, 0.4750651 ],
]

ETHER_1_INSTRUCT="LMAML"


#extraction vessel, ev0 has the vessel without the valve, ev1 has only the valve

EV_0=np.array([[0.42516276, 0.03108724],
       [0.42099609, 0.05192057],
       [0.43349609, 0.06025391],
       [0.43766276, 0.17692057],
       [0.34599609, 0.23108724],
       [0.32516276, 0.30192057],
       [0.34599609, 0.36025391],
       [0.46682943, 0.68108724],
       [0.53317057, 0.68108724],
       [0.65400391, 0.36025391],
       [0.67483724, 0.30192057],
       [0.65400391, 0.23108724],
       [0.56233724, 0.17692057],
       [0.56650391, 0.06025391],
       [0.57900391, 0.05192057],
       [0.57483724, 0.03108724]])

EV_0_INSTRUCT="LLLC,,LLLC,,LLLLLL"

EV_1=np.array([[0.40400391, 0.68108724 ],
       [0.62067057, 0.68108724],
       [0.62067057, 0.7500651 ],
       [0.52483724, 0.7500651 ],
       [0.52483724, 0.76673177],
       [0.55400391, 0.77923177],
       [0.54983724, 0.92089844],
       [0.52483724, 0.92089844],
       [0.52900391, 0.94589844],
       [0.47900391, 0.96673177],
       [0.47067057, 0.9250651 ],
       [0.45400391, 0.92089844],
       [0.45400391, 0.77923177],
       [0.47900391, 0.76673177 ],
       [0.47900391, 0.7500651],
       [0.40400391, 0.7500651],
       [0.40400391, 0.68108724 ]])

EV_1_INSTRUCT="L"*18

#good beaker

B2=np.array([[0.19599609, 0.13772786],
       [0.23349609, 0.1835612 ],
       [0.24599609, 0.21689453],
       [0.24599609, 0.28772786],
       [0.24599609, 0.34189453],
       [0.24599609, 0.46272786],
       [0.24599609, 0.5710612 ],
       [0.24599609, 0.6898112 ],
       [0.25016276, 0.79397786],
       [0.27099609, 0.85647786],
       [0.33349609, 0.88147786],
       [0.43349609, 0.88147786],
       [0.56650391, 0.88147786],
       [0.66650391, 0.88147786],
       [0.72900391, 0.85647786],
       [0.74983724, 0.79397786],
       [0.75400391, 0.6898112 ],
             [0.65400391, 0.6898112 ],
             [0.75400391, 0.6898112 ],
       [0.75400391, 0.5710612 ],
             [0.65400391, 0.5710612 ],
             [0.75400391, 0.5710612 ],
       [0.75400391, 0.46272786],
             [0.65400391, 0.46272786],
             [0.75400391, 0.46272786],
       [0.75400391, 0.34189453],
       [0.75400391, 0.28772786],
       [0.75400391, 0.21689453],
       [0.76650391, 0.1835612 ],
       [0.80400391, 0.13772786]])

B2_INSTRUCT=f"C,,{'L'*4}C,,{'L'*3}C,,{'L'*10}C,,"

B2_WATER = np.array([
       [0.24599609, 0.46272786],
       [0.24599609, 0.5710612 ],
       [0.24599609, 0.6898112 ],
       [0.25016276, 0.79397786],
       [0.27099609, 0.85647786],
       [0.33349609, 0.88147786],
       [0.43349609, 0.88147786],
       [0.56650391, 0.88147786],
       [0.66650391, 0.88147786],
       [0.72900391, 0.85647786],
       [0.74983724, 0.79397786],
       [0.75400391, 0.6898112 ],
       [0.75400391, 0.5710612 ],
       [0.75400391, 0.46272786]])

B2_WATER_INSTRUCT="LLC,,LLLC,,LLL"


TEST_TUBE = [[-0.126, -0.54],
[-0.1125, -0.495],
[-0.1125, -0.45],
[-0.1125, 0.225],
[0.1125, 0.1125, 0, 0, 0, 0.1125, 0.225],
[0.1125, -0.45],
[0.1125, -0.495],
[0.126, -0.54]]
             
             

TEST_TUBE_INSTRUCT = "Q,LALQ,"



#hourglass doesn't have a numpy array base but it probably could have one

def create_curved_hourglass_svg(x,y,width, height, total_time, elapsed_time,s=5):
    # Calculate the sand level based on elapsed time
    sand_level = elapsed_time / total_time
        
        
    path=f"""
    
        <path d="M {0-width/2} {0-height/2} L {0+width/2} {0-height/2} L {0+width*0.43} {0-height/2} 
          C {0+width*0.42} {0-height*0.35}, {0+width*0.3} {0-height*0.2}, {0+width*0.1} {0-height*0.1}
          Q {0} {0} {0+width*0.1} {0+height*0.1} 
          C {0+width*0.3} {0+height*0.2}, {0+width*0.42} {0+height*0.35}, {0+width*0.43} {0+height/2}  

          L {0+width*0.5} {0+height/2} L {0-width*0.5} {0+height/2} L {0-width*0.43} {0+height/2}

          C {0-width*0.42} {0+height*0.35}, {0-width*0.3} {0+height*0.2}, {0-width*0.1} {0+height*0.1}

          Q {0} {0} {0-width*0.1} {0-height*0.1} 

          C {0-width*0.3} {0-height*0.2}, {0-width*0.42} {0-height*0.35}, {0-width*0.43} {0-height/2}

          L {0-width/2} {0-height/2} z" """
    # Define the SVG code for the hourglass shape
    svg_code = f"""
        
      <g transform="translate({x}, {y})">
      <defs>
        <clipPath id="hourglass-clip2">
            {path} />
        </clipPath>
      </defs>
        <rect x="{0-width/2}" y="{0-(height-s)/2 + (height-s)/2*sand_level}" width="{width*2}" height="{(height-s)/2- (height-s)/2*sand_level}" fill="tan" stroke="none" clip-path="url(#hourglass-clip2)"/>
        <rect x="{0-width/2}" y="{0+(height-s)/2 - (height-s)/2*sand_level}" width="{width*2}" height="{(height-s)}" fill="tan" stroke="none" clip-path="url(#hourglass-clip2)"/>

      {path} fill="none" stroke="black" stroke-width="{s*2}"/>
      
      </g>
      
    """
    
    return svg_code


#stop sign function

def stop(x,y,size,sw=5):
    
    angles=np.linspace(0,2*np.pi,9)+np.pi/8
    xs=np.sin(angles)*size
    ys=np.cos(angles)*size
    lines = " ".join([f"{xs[i+1]} {y}" for i,y in enumerate(ys[1:-1])])
    svg_code = f"""
    <g transform="translate({x}, {y})">
        <path d="M {xs[0]} {ys[0]} L {lines}  Z" fill="red" stroke="black" stroke-width="{sw}"/>
        <text x="{-size*0.85}" y="{size*0.2}" font-family="Times New Roman" fill="white" font-size="{size*0.7}">STOP</text>
    </g>
    """
    return svg_code