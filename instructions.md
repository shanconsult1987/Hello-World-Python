# Copilot Instructions for This Repository

## Purpose

** These instructions guide AI-assisted code generation tools (such as GitHub Copilot) to ensure all suggested code aligns with our engineering standards, architecture principles, and maintainability expectations.

## General Engineering Principles

Prioritize readability over cleverness.

Write modular, reusable code.

Avoid unnecessary complexity.

Prefer explicit logic instead of hidden behavior.

Follow SOLID design principles wherever applicable.

## Code Style Requirements
Formatting

Follow the project's configured formatter (e.g., Prettier, Black, ESLint).

Keep functions small and focused.

Use descriptive variable and function names.

## Documentation

Every public function must include:

A clear docstring

Parameter descriptions

Return value description

## Example:

def calculate_total(price: float, tax: float) -> float:
    """
    Calculate the total price including tax.

    Args:
        price: Base price of the item.
        tax: Tax rate as a decimal.

    Returns:
        Final price including tax.
    """
## Type Safety

Always use type hints (Python) or strong typings (TypeScript).

Avoid any unless absolutely necessary.

Prefer typed models over raw dictionaries.

## Error Handling

Do not swallow exceptions.

Provide meaningful error messages.

Fail fast for invalid inputs.

Log errors where appropriate.

## Example:

if price < 0:
    raise ValueError("Price cannot be negative.")
Security Guidelines

Never hardcode secrets, tokens, or credentials.

Use environment variables or secret managers.

Validate all external inputs.

Prefer prepared statements for database queries.

Testing Expectations

When generating code:

Include unit tests whenever possible.

Cover edge cases.

Avoid brittle tests tied to implementation details.

Preferred frameworks:

Python → pytest

JavaScript/TypeScript → Jest

Architecture Preferences

Prefer composition over inheritance.

Separate business logic from infrastructure.

Keep controllers thin and services focused.

Avoid tight coupling between modules.

Performance Awareness

Avoid unnecessary loops or repeated database calls.

Use async patterns when beneficial.

Be mindful of memory usage in large data operations.

When Unsure

If multiple implementations are possible:

👉 Choose the solution that is:

Easier to maintain

Easier to understand

Production-safe

What to Avoid

Over-engineered abstractions

Deprecated libraries

Experimental dependencies without approval

Large functions (>50 lines) unless justified

Copilot Behavior Preference

## When suggesting code:

✅ Prefer production-ready patterns
✅ Explain non-obvious logic via comments
✅ Generate deterministic behavior
✅ Keep dependencies minimal

## Summary

This repository values:

Clarity → Maintainability → Security → Performance

Optimize for long-term sustainability rather than short-term speed.
