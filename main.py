import re
import statistics
from collections import Counter

html_data = """
<html>
<body>
<table>
    <tbody>
    <tr>
        <td>MONDAY</td>
        <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
    </tr>
    <tr>
        <td>TUESDAY</td>
        <td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
    </tr>
    <tr>
        <td>WEDNESDAY</td>
        <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
    </tr>
    <tr>
        <td>THURSDAY</td>
        <td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
    </tr>
    <tr>
        <td>FRIDAY</td>
        <td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
    </tr>
    </tbody>
</table>
</body>
</html>
"""


#cleaning up the data
colors = []
for row in re.findall(r'<td>(.*?)</td>', html_data):
    if ',' in row:
        for c in row.split(','):
            clean = c.strip().upper()
            clean = 'BLUE' if clean == 'BLEW' else 'ASH' if clean == 'ARSH' else clean
            colors.append(clean)

counts = Counter(colors)

#Question 1: mean color of shirt
mean_freq = round(len(colors) / len(counts))
mean_colors = [color for color, count in counts.items() if count == mean_freq]
print(f"1. Mean Color(s): {', '.join(mean_colors)}")



#Question 2: the color of shirt worn the most
mostly_worn = counts.most_common(1)[0][0]
print(f"2. Mostly worn color: {mostly_worn}")

#Question 3: the median color
median_color = sorted(colors)[len(colors) // 2]
print(f"3. Median color: {median_color}")

#Question 4: variance of the color
variance = statistics.pvariance(counts.values())
print(f"4. Variance: {variance:.4f}")

#Question 5: Probability that the color is red
prob_red = counts['RED'] / len(colors)
print(f"5. Probability of RED: {prob_red:.4f} ({prob_red * 100:.2f}%)")

#generating data to store to the database
for color, count in counts.items():
    print(f"{color}:{count}")