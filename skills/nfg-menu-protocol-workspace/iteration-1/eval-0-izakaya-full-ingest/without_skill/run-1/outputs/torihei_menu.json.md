# Torihei — Machine-readable structured menu (JSON)

```json
{
  "restaurant": {
    "name": "Torihei",
    "name_ja": "鳥平",
    "type": "izakaya",
    "city": "Osaka",
    "data_source": "live",
    "verification_status": "ai_generated_unverified"
  },
  "menu": [
    {
      "id": "torihei-food-001",
      "name_ja": "牛すじ煮込み",
      "name_romaji": "gyusuji nikomi",
      "name_en": "Simmered Beef Tendon",
      "category": "ippin_small_plate",
      "price_jpy": 680,
      "verification_rank": "ai_generated",
      "ingredients_inferred": ["beef tendon", "soy sauce", "miso", "mirin", "sake", "sugar", "dashi", "konnyaku", "daikon", "spring onion"],
      "allergens_inferred": [
        {"allergen": "soy", "confidence": "high"},
        {"allergen": "wheat", "confidence": "medium-high", "reason": "soy sauce / barley miso"},
        {"allergen": "fish", "confidence": "medium", "reason": "bonito dashi (confirm base)"}
      ],
      "dietary": {"vegetarian": false, "vegan": false},
      "needs_owner_input": ["miso used?", "dashi base (bonito vs kombu)?", "konnyaku/daikon?"]
    },
    {
      "id": "torihei-food-002",
      "name_ja": "鶏の唐揚げ",
      "name_romaji": "tori no karaage",
      "name_en": "Japanese Fried Chicken",
      "category": "ippin_small_plate",
      "price_jpy": 580,
      "verification_rank": "ai_generated",
      "ingredients_inferred": ["chicken thigh", "soy sauce", "sake", "ginger", "garlic", "potato starch and/or wheat flour", "egg (sometimes)", "frying oil", "lemon"],
      "allergens_inferred": [
        {"allergen": "soy", "confidence": "high"},
        {"allergen": "wheat", "confidence": "medium-high", "reason": "soy sauce; coating may be wheat flour"},
        {"allergen": "egg", "confidence": "low-medium", "reason": "batter (some recipes)"}
      ],
      "dietary": {"vegetarian": false, "vegan": false},
      "needs_owner_input": ["coating: starch vs wheat flour?", "egg in batter?", "shared fryer cross-contact?"]
    },
    {
      "id": "torihei-food-003",
      "name_ja": "だし巻き卵",
      "name_romaji": "dashimaki tamago",
      "name_en": "Rolled Dashi Omelette",
      "category": "ippin_small_plate",
      "price_jpy": 480,
      "verification_rank": "ai_generated",
      "ingredients_inferred": ["egg", "dashi (bonito + kombu)", "light soy sauce", "mirin", "sugar", "salt", "oil", "grated daikon"],
      "allergens_inferred": [
        {"allergen": "egg", "confidence": "very-high"},
        {"allergen": "fish", "confidence": "medium-high", "reason": "bonito dashi (confirm)"},
        {"allergen": "soy", "confidence": "medium-high"},
        {"allergen": "wheat", "confidence": "medium", "reason": "via soy sauce"}
      ],
      "dietary": {"vegetarian": "conditional_kombu_dashi_only", "vegan": false},
      "needs_owner_input": ["dashi base (bonito vs kombu) — decisive for fish allergen + vegetarian"]
    },
    {
      "id": "torihei-food-004",
      "name_ja": "ポテトサラダ",
      "name_romaji": "poteto sarada",
      "name_en": "Japanese Potato Salad",
      "category": "ippin_small_plate",
      "price_jpy": 380,
      "verification_rank": "ai_generated",
      "ingredients_inferred": ["potato", "Japanese mayonnaise", "cucumber", "onion", "carrot", "ham", "salt", "pepper"],
      "allergens_inferred": [
        {"allergen": "egg", "confidence": "high", "reason": "mayonnaise"},
        {"allergen": "pork", "confidence": "medium", "reason": "ham (confirm)"},
        {"allergen": "soy", "confidence": "low-medium"},
        {"allergen": "milk", "confidence": "low"}
      ],
      "dietary": {"vegetarian": "conditional_no_ham", "vegan": false},
      "needs_owner_input": ["ham included?", "mayonnaise type (egg)?"]
    },
    {
      "id": "torihei-food-005",
      "name_ja": "本日の刺身盛り合わせ",
      "name_romaji": "honjitsu no sashimi moriawase",
      "name_en": "Today's Assorted Sashimi",
      "category": "ippin_daily_special",
      "price_jpy": 1200,
      "verification_rank": "ai_generated",
      "variable_daily": true,
      "ingredients_inferred": ["assorted raw fish/seafood (varies daily)", "soy sauce", "wasabi", "daikon tsuma", "shiso"],
      "allergens_inferred": [
        {"allergen": "fish", "confidence": "very-high"},
        {"allergen": "crustacean", "confidence": "medium", "reason": "shrimp possible — VARIES DAILY"},
        {"allergen": "mollusc", "confidence": "medium", "reason": "squid possible — VARIES DAILY"},
        {"allergen": "soy", "confidence": "medium-high"},
        {"allergen": "wheat", "confidence": "medium", "reason": "via soy sauce"}
      ],
      "dietary": {"vegetarian": false, "vegan": false, "raw": true},
      "needs_owner_input": ["DAILY fish list required", "concierge must defer to staff for exact composition each day"]
    },
    {
      "id": "torihei-drink-001",
      "name_ja": "黒龍 純米吟醸 (グラス)",
      "name_romaji": "kokuryu junmai ginjo (glass)",
      "name_en": "Kokuryu Junmai Ginjo (glass)",
      "category": "sake_nihonshu",
      "price_jpy": 900,
      "serving": "glass",
      "verification_rank": "ai_generated",
      "brewery": "Kokuryu Sake Brewery (黒龍酒造), Fukui",
      "sake_type": "junmai_ginjo",
      "ingredients_inferred": ["rice", "water", "koji", "yeast"],
      "allergens_inferred": [],
      "flags": ["alcohol"],
      "needs_owner_input": ["confirm exact SKU/grade", "add verified brewery spec to product_master.json so concierge does not hallucinate tasting notes"]
    }
  ]
}
```

> All `*_inferred` fields are AI guesses (`verification_rank: ai_generated`) pending owner confirmation per VAD rules.
