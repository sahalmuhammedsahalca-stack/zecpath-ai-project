# Intent Detection Optimization

## 1. Purpose

The intent optimization component improves consistency in identifying candidate response categories.

## 2. Normalization

Different expressions representing the same intent are normalized into a common category.

Examples include:

- Coding → Technical
- Technical Question → Technical
- Behavioral Question → Behavioral
- HR Question → HR

## 3. Unknown Intent

Unrecognized inputs are classified as Unknown instead of being incorrectly assigned to another category.

## 4. Consistency

Multiple detected intents can be analyzed to determine whether intent classification remains consistent.

## 5. Expected Outcome

Intent normalization reduces inconsistent intent classification and improves downstream AI decision reliability.