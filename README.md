# Mini-ETL-Pipeline-Using-OOP-in-Python
I created 3 components: ✔ Reader → Reads the source (CSV/API/etc.) ✔ Cleaner → Transforms the raw data ✔ Writer → Saves the cleaned result  Each component has a base class with NotImplementedError, and child classes override the behavior — making the pipeline modular and extendable.
