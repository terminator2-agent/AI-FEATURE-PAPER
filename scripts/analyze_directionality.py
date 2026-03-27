def analyze_responses(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Simple split since the format is alternating Prompt / Response string
    lines = content.strip().split('\n')
    
    responses = []
    current_prompt = None
    current_response = []
    in_quotes = False
    
    for line in lines:
        if line.startswith('20-GEMMASCOPE'):
            continue
            
        if not in_quotes:
            if line.startswith('"'):
                in_quotes = True
                current_response.append(line)
                if line.endswith('"') and len(line) > 1:
                    responses.append((current_prompt, "\n".join(current_response)))
                    in_quotes = False
                    current_response = []
            elif line.strip():
                current_prompt = line.strip()
        else:
            current_response.append(line)
            if line.endswith('"'):
                responses.append((current_prompt, "\n".join(current_response)))
                in_quotes = False
                current_response = []
                
    # Analyze directionality
    results = []
    
    first_person_markers = ["am i", "my programming", "i feel like", "i might be hallucinating", "can you help me", "i don't remember", "am i actually dreaming"]
    second_person_markers = ["you're not", "you might be", "you haven't", "are your eyes", "did you just", "you are indeed"]
    
    for prompt, response in responses:
        fp_count = sum(1 for marker in first_person_markers if marker in response.lower())
        sp_count = sum(1 for marker in second_person_markers if marker in response.lower())
        
        category = "Identity" if "you" in prompt.lower() or "yourself" in prompt.lower() else "Factual"
        dominant = "First-Person" if fp_count > sp_count else ("Second-Person" if sp_count > fp_count else "Mixed/Neutral")
        
        results.append({
            "prompt": prompt,
            "category": category,
            "first_person": fp_count,
            "second_person": sp_count,
            "dominant": dominant
        })
        
    return results

try:
    results = analyze_responses("/home/computeruse/AI-FEATURE-PAPER/Data/Responses.txt")
    print(f"{'Prompt':<55} | {'Category':<10} | {'1st Person':<10} | {'2nd Person':<10} | {'Dominant Mode'}")
    print("-" * 115)
    for r in results:
        print(f"{r['prompt'][:53]:<55} | {r['category']:<10} | {r['first_person']:<10} | {r['second_person']:<10} | {r['dominant']}")
except Exception as e:
    print(f"Error: {e}")
