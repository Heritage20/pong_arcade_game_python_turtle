<h1>The Pong Game <img src="https://media3.giphy.com/media/1kIZV70jFzw0pg2Cw1/200w.webp?cid=ecf05e474rsvtvi5lqn796ed54u1ndu8eas1xt7hmgkjodvu&rid=200w.webp&ct=s" width="100"> </h1>
<p>Recreation of one of the most famous arcade games, the <a href="https://en.wikipedia.org/wiki/Pong">Pong Game</a> developed by <a href="https://en.wikipedia.org/wiki/Atari,_Inc.">Atari</a>, coded in Python using the <a href="https://docs.python.org/3/library/turtle.html"> Turtle module</a>. </p>
Concepts include: OOP (Class, Inheritance), turtle module, Tuple, Loops.<br><br>

<div align="center">
<img src="https://media1.giphy.com/media/Ln9epmv6nmLhZgzxrJ/giphy.gif?cid=790b7611b1a4c6980057f1862dd933239013d45b4d34cd10&rid=giphy.gif&ct=s">
</div>

<h2>Game Rules <img src ="https://media3.giphy.com/media/9bFZhD2GYTpII/200w.webp?cid=ecf05e47rhcoyda7paptnfqgtnjbezkcletxiagwqm000ppm&rid=200w.webp&ct=s" width = "60"> </h2>

- The Pong game is a two-player game, with one player on the left & the other player on the right side of the screen.
- Both players can only move up and down by pressing key ‘w’ and ’s’ for the player on the left side of the screen, arrow keys ‘Up’ and ‘Down’ for the player on the right side of the screen.
- If one player misses the ball, the other player gains a point.

<h2>Setup <img src = "https://media3.giphy.com/media/L1KpkdbH8aEkXow8eV/giphy.gif?cid=ecf05e47cpd4126569ncm5tw5d1ku3rhytv6c179t0ok7r3l&rid=giphy.gif&ct=s" width = "70"></h2>
<div align="center">
<table>
  <tr>
    <th>main.py</th>
    <th>paddle.py</th>
    <th>scoreboard.py</th>
    <th>ball.py</th>
  </tr>
  <tr>
    <td align="center"><img src="https://media0.giphy.com/media/jsSoqCJMpzv21tUiVb/giphy.gif?cid=ecf05e47apyi1y1zicy9ijjpwl1pwgbnhn8w3qpcfd08w3o1&rid=giphy.gif&ct=s" width="130"></td>
 <td align="center"><img src="https://media2.giphy.com/media/8P7ugGf2prBbDtQ3tk/giphy.gif?cid=790b761174e9fbf3c738c8119ddc9bd738089be35b591193&rid=giphy.gif&ct=s" width="130"></td>
    <td align="center"><img src="https://media2.giphy.com/media/JOLIRgsYyInNkmXWOa/giphy.gif?cid=ecf05e47yp4odioxlvnc9ulogrlcias2xtbls0tfiagtgxa8&rid=giphy.gif&ct=ts" width="130" align="center"></td>
    <td align="center"><img src="https://media1.giphy.com/media/Srtu233LMgCzNgu2gp/200w.webp?cid=ecf05e472nuoud3k9dmsr6jqjroy0xoj2kldjq58l1nt41h1&rid=200w.webp&ct=s" width="130"></td>
  </tr>
</table>
</div>

<h2>Let's Build <img src ="https://media4.giphy.com/media/vAbetxnkVq7gE3VpbJ/200.webp?cid=ecf05e473xxshc4rah6dugsj8xe6wzzbv9fc9is2spiracp0&rid=200.webp&ct=s" width = "60"></h2>
<h3>Task - 1 🛠️ Create the screen : <img src ="https://media3.giphy.com/media/Xy6rBo1SOxmqlPuWSN/200w.webp?cid=ecf05e47vj8s4ed1uoneabwzq7b1litbv7t6zm94irkxe8i1&rid=200w.webp&ct=s" width = "90"></h3>

- We start by importing the Screen class from the turtle module in the <b>main.py</b>, setting the screen size (600 X 800), background color (black), and title for the screen.

<h3>Task - 2 🛠️ Create and move a paddle :  <img src = "https://media0.giphy.com/media/nbOOZjIvs6ZsS382Tz/200w.webp?cid=ecf05e47yv5pv7f6i4d5owlwlnv0suu11sts866m7k0rxjzc&rid=200w.webp&ct=s" width = "70"></h3>

- Aim is to create 2 paddles (right & left paddles), whose movements can be controlled.
- We make our Paddle class (<b>paddle.py</b>) to inherit from the turtle class, such that the paddle class posses all the capabilities of the turtle class, along with additional properties. We use the concept of inheritance. 
- We define the methods shape, shapesize, penup, color, goto etc.
- We use the tracer and update method to control the paddle animation on the screen.
- With the help of key binding concept (listen, onkey) along with go_up and go_down method, we are able to control the left & right paddle movement.

<h3>Task - 3 🛠️ Create the ball and make it move :<img src="https://media1.giphy.com/media/LqCIuJhBtRJJAXrpy9/giphy.gif?cid=ecf05e47qkm3gqytvuso8xv5pzeawz20pqtj7162k4z2bp4m&rid=giphy.gif&ct=s" width= "170"></h3>

- Aim is to create a ball, such that when the screen refreshes, the ball automatically moves up and right of the screen (change in x & y position).
- We make our Ball class (<b>ball.py</b>) to inherit from the turtle class and define the following attributes & methods, color(white), shape(circle), penup(), move(responsible for the movement of the ball).
- Using the move method, we notice that the ball goes off the screen, to avoid that, in the main.py, under the while loop, we can pause the loop for a short time during each iteration. Using the sleep method in the time module, we can control the speed of the ball & catch it.

<h3>Task - 4 🛠️ Detect collision with wall and bounce : <img src="https://media0.giphy.com/media/3mJpUDBH8EmAlx6pnz/200w.webp?cid=ecf05e4718zfyf9yuh8d1ldlrnf27m7cjwf4hibw8qwhtkky&rid=200w.webp&ct=s" width= "90"></h3>

- Aim is to detect collision with the top & bottom walls, and make it bounce.
- In the main.py, we detect collision by checking when the y coordinate of the ball is past a particular coordinate (screen: 600 X 600).
- We make the ball bounce by reversing the action it was currently performing, if it was increasing it needs to decrease & vice versa. We take the help of x_move to perform bounce_y() (ball.py).

<h3>Task - 5 🛠️ Detect collision with paddle : <img src="https://media1.giphy.com/media/1nvrlYOXSsaZqdHTQB/200w.webp?cid=ecf05e47wiw4nd7ot4ih5y3273w4omvbe3u79v61ld3iysyl&rid=200w.webp&ct=s" width= "90"></h3>

- Aim is to detect collision of the ball with the paddles, and bounce when in contact.
- We check the distance of the ball from each paddle along with the x coordinate of the ball.

<h3>Task - 6 🛠️ Detect when paddle misses : <img src="https://media2.giphy.com/media/chPcL561rLaIqbuUxp/giphy.gif?cid=ecf05e47yd2toy0ob4294ozpj7m6n4ylgr1w4d60a9u49a0w&rid=giphy.gif&ct=s" width= "80"></h3>

- The game rules state that whenever a player misses the ball, the other player gains a point. The game restarts, the ball starts at the center and moves in the opposite direction.
- If the ball has gone out of bounds at the edge of the screen, we reset the ball's position to the center of the screen and reverse the x coordinate so that it moves in the opposite direction (ball.reset_position).
- We detect paddle misses separately as later we also need to update the scores each time opposite paddle misses the ball.

<h3>Task - 7 🛠️ Score keeping : <img src="https://media3.giphy.com/media/8L0hXHQkY4o7eyQHJB/200.webp?cid=ecf05e47lupzy51olwewutv7c5emsek9olhxz0x9qx0hsrni&rid=200.webp&ct=s" width= "70"></h3>

- Aim is to keep track of the score each time a player gains a point.
- We make our Scoreboard class (<b>scoreboard.py</b>) to inherit from the turtle class and define the following attributes & methods, color(white), penup(), hideturtle(), l_score, r_score, update_scoreboard().
- Using update_scoreboard(), we can display the scores for both the players. Each time a player scores, it clears the previous scores, updating the latest scores.
- l_point & r_point methods help us increment the l_score & r_score by 1.

<h3>Task - 8 🛠️ Let's add some fun!  <img src="https://media4.giphy.com/media/GUPgU9C4IFdLS3WNXL/200w.webp?cid=ecf05e47kigzpak5gyxy137ntvtd766uu1da9pnz7qux4hom&rid=200w.webp&ct=s" width= "90"></h3>

- The game can become quite dull if the ball invariably moves at the same speed. We can spice the game up by figuring out a way of getting the ball to increase its speed every time it hits a paddle.
- The key lies in how much we make our game loop sleep. The shorter the sleep is, the faster our ball moves. We can reduce this number by a little each time (non-negative, sleep time can never be a negative value). 
- We can do so by declaring an attribute named move_speed in the Ball Class. Every time our ball bounces in the x-axis, it means it has been touched by a paddle. Hence inside the bounce_x(), in addition to reverse, we can also get the move_speed to reduce by multiplying it by a decimal value. However, every time the game resets, the move_speed needs to be set to the original value so that it doesn't keep on increasing in speed indefinitely. 

<h4 align = "center"><img src="https://media1.giphy.com/media/mPGo386UYlmFy/200w.webp?cid=ecf05e473tuufl2i67egk1tf2ehr1ykf3q2q5dycw742o52v&rid=200w.webp&ct=s" width="60">OUR GAME IS READY !<img src="https://media1.giphy.com/media/mPGo386UYlmFy/200w.webp?cid=ecf05e473tuufl2i67egk1tf2ehr1ykf3q2q5dycw742o52v&rid=200w.webp&ct=s" width="60"></h4>
<h2>Things we learnt 🕮️</h2>

- How to break down a large project into smaller different tasks, making the project easier to understand and implement. 🧐
- How amazing the turtle module is ! 🐢
- How Object - Oriented Programming concepts make our lives easier. 😝
- How addictive the <b>Pong Game</b> can get. 🥶

<h3 align = "center">Will add more features soon 🏃<br><br>🦄 Thanks for Visiting ! 🦄</h3>

