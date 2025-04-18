import csv
import matplotlib.pyplot as plt

protocols = ['vegas', 'cubic', 'bbr']
rtts = []
throughputs = []

for proto in protocols:
    # Get average RTT
    with open(f'{proto}_stats.csv', 'r') as stats_file:
        reader = csv.DictReader(stats_file)
        stats = {row['Metric']: float(row['Value']) for row in reader}
        rtts.append(stats['Average RTT (ms)'])

    # Get average throughput from CSV
    with open(f'{proto}_throughput.csv', 'r') as throughput_file:
        reader = csv.reader(throughput_file)
        next(reader)  # skip header
        values = [float(row[1]) for row in reader]
        avg_throughput = sum(values) / len(values)
        throughputs.append(avg_throughput)

# Plot RTT vs Throughput
plt.figure()
plt.scatter(rtts, throughputs, color='blue', s=100)

for i, proto in enumerate(protocols):
    plt.text(rtts[i] + 1, throughputs[i], proto.upper(), fontsize=10)

plt.xlabel('Average RTT (ms)')
plt.ylabel('Average Throughput (Mbps)')
plt.title('RTT vs. Throughput Summary Graph')
plt.grid(True)
plt.tight_layout()
plt.savefig('rtt_vs_throughput.png')
print(" Saved: rtt_vs_throughput.png")
