# midi-sorter
Simple Python script meant to sort specific MIDI grooves into SSD 5 compatible folders.

- Checks which MIDI files belong to same category. For example, "132bpmExample1.mid" and "132bpmExample2.mid" belong to same category.
- Creates a directory for that category. For example: creates directory "132bpmExample.prt" where "132bpmExample1.mid" and "132bpmExample2.mid" should go.
- Moves all matching .mid files into the created directory.

# How to use
Just place midi-sorter.py into folder you want to sort and run it.