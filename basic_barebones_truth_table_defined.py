"""
∀d ∈ ℝ⁺ : (d = 333.33092) → (convert_dewey_to_bo(d) = 42.1)            # ⊤
For every Dewey Decimal number equal to 333.33092, the mapping returns the Bo-system
class mark 42.1 (Business Negotiation).                                # True
Real-world: lets librarians shelve **Trump — 《交易的艺术》** alongside other
negotiation titles under a custom Bo Dewie System.                      # Works in any physical or digital catalog
"""

# citation: :contentReference[oaicite:0]{index=0}

from dataclasses import dataclass

# --- Mapping tables -----------------------------------------------------------

DEWEY_TO_BO = {
    # Donald Trump, Tony Schwartz – *The Art of the Deal*
    # Dewey 333.33092 B → Bo 42.1
    "333.33092": "42.1",  # Business → Negotiation / Deal-making
}

# --- Core functions -----------------------------------------------------------

def convert_dewey_to_bo(ddc: str) -> str:
    """
    ∀x ∈ Dom(DEWEY_TO_BO) : convert_dewey_to_bo(x) = DEWEY_TO_BO[x]      # ⊤
    For every key present in the mapping, the function returns its value.
    Practical: enables catalog migration from Dewey to Bo Dewie numbers.  # Libraries & personal DBs
    """
    return DEWEY_TO_BO.get(ddc, "Unclassified")


@dataclass(frozen=True)
class BookRecord:
    title_en: str
    title_zh: str
    isbn: str
    dewey: str
    bo_class: str


def find_art_of_the_deal_chinese() -> BookRecord:
    """
    ⊤ ↔ (book.isbn = 7515342633 ∧ book.dewey = 333.33092)                # ⊤
    The Chinese edition of *The Art of the Deal* has ISBN 7515342633 and
    Dewey 333.33092, mapping to Bo 42.1.                                  # True
    Real-world: quickly fetches metadata for ordering or shelving the
    Chinese translation in any system adopting Bo codes.                  # Useful for librarians & readers
    """
    return BookRecord(
        title_en="Trump: The Art of the Deal",
        title_zh="交易的艺术",
        isbn="7515342633",
        dewey="333.33092",
        bo_class=convert_dewey_to_bo("333.33092"),
    )


# --- Optional: propositional-truth-table encoder ------------------------------

def truth_table_to_bpe(table: list[tuple[bool, bool]]) -> list[int]:
    """
    ∀(p,q)∈table : r = p ∧ q ⇒ encode(r) = 1 if r else 0                 # ⊤
    Given a truth table for conjunction, map each output to a toy BPE
    id (1 for True, 0 for False).                                         # True
    Applicability: demonstrates how logical outcomes may become token
    logits inside a transformer’s softmax layer for educational demos.    # Pedagogical
    """
    # Toy encoder: ⊤→1, ⊥→0
    return [1 if (p and q) else 0 for p, q in table]


# -------------------------- Example (will run if executed) --------------------

if __name__ == "__main__":
    # Map Dewey → Bo
    print(convert_dewey_to_bo("333.33092"))  # 42.1

    # Fetch book metadata
    record = find_art_of_the_deal_chinese()
    print(record)

    # Encode a truth table
    sample = [(False, False), (True, False), (True, True)]
    print(truth_table_to_bpe(sample))  # [0, 0, 1]
