import heapq

# Node structure
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # for priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(text):

    if not text:
        return {}, ""
    # Step 1: Frequency of each character
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    # Step 2: Create a priority queue (min-heap)
    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    # Step 3: Build Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    root = heap[0]

    # Step 4: Generate Huffman Codes
    huffman_codes = {}

    def generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            huffman_codes[node.char] = current_code or "0"
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")

    # Step 5: Encode the text
    encoded_text = "".join(huffman_codes[ch] for ch in text)

    return huffman_codes, encoded_text


# Example usage
text = "greedystrategy"
codes, encoded = huffman_encoding(text)

print("Character\tHuffman Code")
for ch, code in codes.items():
    print(f"{ch}\t\t{code}")

print("\nEncoded Text:", encoded)
