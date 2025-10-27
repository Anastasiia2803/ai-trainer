```python
import click

WORKOUTS = [
    ("Day 1", "Upper body push: bench press 5x5, dips 3x8"),
    ("Day 2", "Lower body: squats 5x5, lunges 3x10/leg"),
    ("Day 3", "Engine: 20min EMOM (10 burpees / 10 air squats)"),
    ("Day 4", "Pull: deadlift 5x3, pull-ups 5x max"),
    ("Day 5", "Core + conditioning: plank 5x60s, 5 rounds 500m row"),
    ("Day 6", "Active recovery: 45 min zone2"),
    ("Day 7", "Mobility + light cardio 30 min"),
]

@click.command()
@click.option("--goal", default="balance", help="gain muscle / cut / balance")
@click.option("--days", default=7, type=int)
def cli(goal, days):
    print(f"AI-Trainer plan ({goal}, {days} days)")
    for i in range(min(days, len(WORKOUTS))):
        d, w = WORKOUTS[i]
        print(f"{d}: {w}")

if __name__ == "__main__":
    cli()
