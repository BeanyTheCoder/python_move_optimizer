# Move Optimizer Project 🐾

A simple function that calculates the resultant movement based on given cardinal directions (\***\*NORTH**, **SOUTH**, _EAST_, **WEST\*\***) and returns the simplified path.

## Original problem

### Direction Catastrophe

A very simple problem with many different solutions, but the main aim is to solve it in the most efficient way. A man was given directions to go from point A to point B. The directions were: "**SOUTH\*", "**NORTH*", "*WEST*", "*EAST*". Clearly "*NORTH*" and "*SOUTH*" are opposite, "*WEST*" and "*EAST\*" too. Going to one direction and coming back in the opposite direction is a waste of time and energy. So, we need to help the man by writing a program that will eliminate the useless steps and will contain only the necessary directions.

For example: The directions ["*NORTH*", "*SOUTH*", "*SOUTH*", "*EAST*", "*WEST*", "*NORTH*", "*WEST*"] should be reduced to ["*WEST*"]. This is because going "_NORTH_" and then immediately "_SOUTH_" means coming back to the same place. So we cancel them and we have ["*SOUTH*", "*EAST*", "*WEST*", "*NORTH*", "*WEST*"]. Next, we go "_SOUTH_", take "_EAST_" and then immediately take "_WEST_", which again means coming back to the same point. Hence we cancel "_EAST_" and "_WEST_" to giving us ["*SOUTH*", "*NORTH*", "*WEST*"]. It’s clear that "_SOUTH_" and "_NORTH_" are opposites hence canceled and finally we are left with ["*WEST*"].

## Features ✨

- ✅ Reduces redundant movements by implementing simple vector maths

## Installation & Usage 🛠️

1. Clone the repository using:

   ```sh
   git clone https://github.com/BeanyTheCoder/move_optimizer
   ```

2. Navigate to the project directory using:

   ```sh
   cd move_optimizer
   ```

3. Run the script:
   ```sh
   python main.py
   ```

### Example Usage

```python
print(move("NORTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "EAST"))
# Output: ['**NORTH**']
```

## Technologies Used 🛠️

- Python

## License 📝

This project is licensed under the [MIT License](LICENSE).

## Author 👤

My name is **Alexander Afoko Jnr**, a passionate 15-year-old programmer from Ghana.

I'm focused on expanding my portfolio and improving my skills as a programmer.

## Contact 📧

- **Gmail** - alexanderafoko@gmail.com
- **GitHub** - [BeanyTheCoder](https://github.com/BeanyTheCoder)
- **Frontend Mentor** - [@BeanyTheCoder](https://www.frontendmentor.io/profile/BeanyTheCoder)
- **Discord** - beanythecoder
