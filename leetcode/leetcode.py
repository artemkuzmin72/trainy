import random

words = {
    # A
    "able": "способный",
    "additional": "дополнительный",
    "adversarial": "состязательный",
    "approach": "подход",
    "augment": "увеличение",

    # B
    "benefit": ["выгода, польза"],
    "broad": "широкий",

    # C
    "consider": "рассматривать",
    "convergence": "сходимость",
    "convolutional": "сверточный",
    "conversely": "наоборот",
    "counterparts": ["копия, аналог"],
    "cuisine": "кухня",
    "curves": "кривые",

    # D
    "dense": "плотный",
    "desire": "желание",
    "determine": "определять",

    # E
    "efforts": "усилия",
    "either": "либо, или",
    "embedding": "встраивание",
    "emphasizing": "подчеркивая",
    "ensure": "гарантировать",
    "evaluate": "оценивать",
    "even": "даже",
    "estimators": "оценщики",
    "exercise": "упражнение",
    "expansion": "расширение",
    "extensive": "обширный",

    # F
    "feasible": "осуществимый",
    "feature": "особенность",
    "fitting": "оснащен",

    # G
    "gap": ["пробел, разрыв"],
    "gather": "собирать",
    "generalization": "обобщение",

    # I
    "implications": "последствия",
    "inference": "вывод",
    "influence": "влияние",
    "instead": "вместо",
    "introduce": "представлять",
    "infused": "насыщенный",

    # K
    "kernel": "ядро",

    # L
    "label": "метка",
    "leverage": "использовать",

    # M
    "magnitude": "величина",
    "measurements": "размеры",
    "moreover": "более того",

    # N
    "nonsense": "ерунда",

    # O
    "occurs": "происходит",
    "often": "часто",
    "operate": "работать",
    "origin": "источник",
    "outliers": "выбросы",
    "overfitting": "переобучение",

    # P
    "perform": "выполнять",
    "performance": ["представление, производительность"],
    "plot": "сюжет",
    "precission": "точность",
    "prevent": ["избегать, предотвращать"],
    "prominent": ["важный, значимый"],
    "prune": ["обрезать, сокращать"],

    # R
    "rather": "скорее",
    "recall": "отзыв",
    "reduce": ["сокращать, уменьшать"],
    "referred": "направленный",
    "refers": "относится",
    "related": "связанный",
    "relatively": "относительно",
    "requir": "требовать",
    "revolve": "вращаться",

    # S
    "sacrificing": "жертвуя",
    "significant": ["существенно, значительно"],
    "slope": "наклон",
    "sparse": "разреженный",
    "species": "вид",
    "spurious": ["поддельный, ложный"],
    "stood": "выдержавший",
    "subsequent": "последующий",
    "suffers": "страдает",
    "suggests": "предполагает",

    # T
    "though": "хотя",

    # U
    "underlying": "фундаментальный",
    "unsuitable": "неподходящий",
}

for key, value in list(words.items()):
    if isinstance(value, str):
        words[key] = [value]

word_list = list(words.items())
random.shuffle(word_list)

keys = list(words.keys())
random.shuffle(keys)

problems = {}

count = 0 
words_count = 0

for english, russian_list in word_list:
    print(f"Guess the translation for: {english}")
    user_input = input("Your answer: ").strip().lower()

    # Проверяем команды выхода
    if user_input in ['exit', 'стоп', 'stop']:
        print("\n🚪 Вы вышли из тренировки.")
        break

    # Проверяем правильный ответ
    if user_input in [r.lower() for r in russian_list]:
        print("✅ Correct!\n")
        count += 1
    else:
        print(f"❌ Wrong! Correct answers: {', '.join(russian_list)}\n")
        problems[english] = russian_list
    words_count += 1

print(f"\n🏁 Your total score: {count} out of {words_count}")
if problems:
    print("📚 Problem words:")
    for eng, rus in problems.items():
        print(f"  {eng} → {', '.join(rus)}")
else:
    print("🎉 Отлично! Нет проблемных слов.")