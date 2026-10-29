const pptxgen = require('pptxgenjs');
const fs = require('fs');

const pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';

// Branding Palette
const COLORS = {
  bg_dark: '0B0F1A',   // Deep navy/black
  bg_card: '161B2C',   // Slightly lighter navy
  accent: '00A3FF',    // Bright blue
  text_main: 'FFFFFF', // White
  text_muted: 'A0AEC0', // Gray
  danger: 'FF4D4D',    // Red
  success: '00C853',   // Green
};

const THEME = {
  name: 'QuantumShield Theme',
  headFontFace: 'Arial',
  bodyFontFace: 'Calibri',
  colors: {
    dk1: COLORS.bg_dark,
    lt1: COLORS.bg_card,
    dk2: '000000',
    lt2: 'FFFFFF',
    accent1: COLORS.accent,
    accent2: '007ACC',
    accent3: '00C853',
    accent4: 'FFB800',
    accent5: 'FF4D4D',
    accent6: 'A0AEC0',
    hlink: COLORS.accent,
    folHlink: COLORS.accent,
  }
};

// Layouts
pres.defineSlideMaster({
  title: 'Standard',
  background: { fill: COLORS.bg_dark },
  objects: [
    { rect: { x: 0, y: 0, w: '100%', h: 0.6, fill: { color: COLORS.bg_card } }, objectName: 'header_bar' },
    { text: { text: 'QuantumShield', options: { x: 0.3, y: 0.2, w: 2, h: 0.3, fontSize: 14, color: COLORS.accent, bold: true, align: 'left' } }, objectName: 'logo' },
    { text: { text: 'Post-Quantum Readiness Platform', options: { x: 0.3, y: 0.4, w: 3, h: 0.1, fontSize: 8, color: COLORS.text_muted, align: 'left' } }, objectName: 'tagline' },
  ],
});

// Helper for consistent cards
function addCard(slide, x, y, w, h, title, content, color = COLORS.accent) {
  slide.addShape(pres.ShapeType.roundRect, { x, y, w, h, fill: { color: COLORS.bg_card }, line: { color: color, width: 1 }, rectRadius: 0.1 });
  slide.addText(title, { x: x + 0.1, y: y + 0.1, w: w - 0.2, h: 0.3, fontSize: 12, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });
  slide.addText(content, { x: x + 0.1, y: y + 0.4, w: w - 0.2, h: h - 0.5, fontSize: 10, color: COLORS.text_muted, align: 'left', isTextBox: true });
}

// --- SLIDE 1: TITLE ---
const s1 = pres.addSlide({ masterName: 'Standard' });
s1.background = { fill: COLORS.bg_dark };
s1.addText('QuantumShield', { x: 1, y: 1.5, w: 8, h: 1, fontSize: 44, color: COLORS.accent, bold: true, align: 'center', isTextBox: true });
s1.addText('Cryptographic Risk Intelligence & Post-Quantum Readiness Platform', { x: 1, y: 2.4, w: 8, h: 0.5, fontSize: 20, color: COLORS.text_main, align: 'center', isTextBox: true });
s1.addText('Discover. Quantify. Prioritize. Migrate.', { x: 1, y: 2.9, w: 8, h: 0.4, fontSize: 16, color: COLORS.text_muted, italic: true, align: 'center', isTextBox: true });
s1.addText('Team Diet Claude | MG Solutions Build Spark Hackathon', { x: 1, y: 4.5, w: 8, h: 0.3, fontSize: 12, color: COLORS.text_muted, align: 'center', isTextBox: true });
s1.addText('https://quantumshield-seven.vercel.app', { x: 1, y: 4.8, w: 8, h: 0.3, fontSize: 12, color: COLORS.accent, align: 'center', isTextBox: true });
// Note: Screenshot would go here. Placeholder image for logic.
s1.addImage({ path: '/sessions/trusting-laughing-lamport/mnt/QuantumShield/tests/results/e2e_01_dashboard.png', x: 2.5, y: 3.2, w: 5, h: 1.2 });

// --- SLIDE 2: THE PROBLEM ---
const s2 = pres.addSlide({ masterName: 'Standard' });
s2.addText('Your organization cannot migrate cryptography it cannot see.', { x: 0.3, y: 0.7, w: 9, h: 0.5, fontSize: 24, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });

// Grid for hidden assets
const assets = [
  'Source Code', 'Dependencies', 'X.509 Certificates',
  'Keystores', 'Server Configurations', 'JVM Bytecode'
];
assets.forEach((asset, i) => {
  const col = i % 3;
  const row = Math.floor(i / 3);
  addCard(s2, 0.3 + col * 3.2, 1.3 + row * 1.2, 3, 1, 'Hidden Asset', asset, COLORS.text_muted);
});

s2.addText('The Quantum Consequences:', { x: 0.3, y: 4.1, w: 9, h: 0.3, fontSize: 16, color: COLORS.accent, bold: true, align: 'left', isTextBox: true });
s2.addText('Shor: Breaks RSA/ECC/DH | Grover: Halves Symmetric Security | HNDL: Retroactive Decryption | TNFL: Retroactive Forgery', { x: 0.3, y: 4.4, w: 9, h: 0.5, fontSize: 12, color: COLORS.text_main, align: 'left', isTextBox: true });

// --- SLIDE 3: OUR SOLUTION ---
const s3 = pres.addSlide({ masterName: 'Standard' });
s3.addText('QuantumShield turns invisible cryptography into actionable risk intelligence.', { x: 0.3, y: 0.7, w: 9, h: 0.5, fontSize: 24, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });

// Workflow flow
const workflow = ['DISCOVER', 'INVENTORY', 'ANALYZE', 'PRIORITIZE', 'REMEDIATE', 'MONITOR'];
workflow.forEach((step, i) => {
  s3.addShape(pres.ShapeType.roundRect, { x: 0.3 + i * 1.6, y: 2.0, w: 1.4, h: 0.6, fill: { color: COLORS.bg_card }, line: { color: COLORS.accent, width: 1 }, rectRadius: 0.1 });
  s3.addText(step, { x: 0.3 + i * 1.6, y: 2.1, w: 1.4, h: 0.4, fontSize: 10, color: COLORS.text_main, bold: true, align: 'center', isTextBox: true });
});

s3.addText('Offline-first | Evidence-backed | Standards-native | Migration-oriented', { x: 0.3, y: 3.2, w: 9, h: 0.3, fontSize: 14, color: COLORS.text_muted, italic: true, align: 'center', isTextBox: true });
s3.addImage({ path: '/sessions/trusting-laughing-lamport/mnt/QuantumShield/tests/results/e2e_01_dashboard.png', x: 2, y: 3.5, w: 6, h: 1.8 });

// --- SLIDE 4: HOW IT WORKS ---
const s4 = pres.addSlide({ masterName: 'Standard' });
s4.addText('A six-stage cryptographic intelligence pipeline', { x: 0.3, y: 0.7, w: 9, h: 0.5, fontSize: 24, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });

const stages = [
  { t: '01 Discovery', d: 'Source, deps, certs, keystores, configs, bytecode' },
  { t: '02 Evidence', d: 'Normalization: File + line + snippet + confidence' },
  { t: '03 Deduplication', d: 'Normalized path + line + algorithm + usage' },
  { t: '04 Classification', d: 'Shor-broken / Grover-weakened / safe' },
  { t: '05 Risk Modeling', d: 'Mosca inequality + 5-factor risk score' },
  { t: '06 Remediation', d: 'PQC recommendations + CBOM + reports' },
];
stages.forEach((s, i) => {
  addCard(s4, 0.3 + (i % 2) * 4.7, 1.3 + Math.floor(i / 2) * 1.3, 4.5, 1.1, s.t, s.d);
});

// --- SLIDE 5: QUANTUM RISK ENGINE ---
const s5 = pres.addSlide({ masterName: 'Standard' });
s5.addText('From algorithm detection to measurable business risk', { x: 0.3, y: 0.7, w: 9, h: 0.5, fontSize: 24, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });

s5.addText('Mosca\'s Inequality: X + Y > Z', { x: 0.3, y: 1.3, w: 4, h: 0.4, fontSize: 20, color: COLORS.accent, bold: true, align: 'left', isTextBox: true });
s5.addText('X: Migration Time | Y: Security Lifetime | Z: CRQC Horizon', { x: 0.3, y: 1.6, w: 6, h: 0.3, fontSize: 12, color: COLORS.text_muted, align: 'left', isTextBox: true });

// Risk Table
s5.addShape(pres.ShapeType.rect, { x: 5, y: 1.3, w: 4, h: 3, fill: { color: COLORS.bg_card }, line: { color: COLORS.text_muted, width: 1 } });
s5.addText('5-Factor Risk Model', { x: 5.1, y: 1.4, w: 3.8, h: 0.4, fontSize: 16, color: COLORS.text_main, bold: true, align: 'center', isTextBox: true });
s5.addText('Quantum Exposure (35%)\nBusiness Criticality (25%)\nExposure Surface (15%)\nData Sensitivity (15%)\nInversed Agility (10%)', { x: 5.1, y: 1.8, w: 3.8, h: 2, fontSize: 12, color: COLORS.text_muted, align: 'left', isTextBox: true });
s5.addText('Output: 0-100 Risk Score (Critical / High / Medium / Low)', { x: 5, y: 4.3, w: 4, h: 0.3, fontSize: 12, color: COLORS.accent, bold: true, align: 'center', isTextBox: true });

// --- SLIDE 6: POST-QUANTUM MIGRATION ---
const s6 = pres.addSlide({ masterName: 'Standard' });
s6.addText('From finding → recommendation → migration plan', { x: 0.3, y: 0.7, w: 9, h: 0.5, fontSize: 24, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });

s6.addText('Vulnerable Classical', { x: 1, y: 1.5, w: 3, h: 0.4, fontSize: 14, color: COLORS.danger, bold: true, align: 'center', isTextBox: true });
s6.addText('ML-KEM / ML-DSA / SLH-DSA', { x: 5, y: 1.5, w: 4, h: 0.4, fontSize: 14, color: COLORS.success, bold: true, align: 'center', isTextBox: true });
s6.addShape(pres.ShapeType.line, { x: 4, y: 1.7, w: 1, h: 0, line: { color: COLORS.accent, width: 2 } });

s6.addText('NIST FIPS 203 / 204 / 205 Standards Mapping', { x: 0.3, y: 2.5, w: 9, h: 0.3, fontSize: 14, color: COLORS.text_muted, align: 'center', isTextBox: true });
s6.addImage({ path: '/sessions/trusting-laughing-lamport/mnt/QuantumShield/tests/results/e2e_06_migration.png', x: 2, y: 3, w: 6, h: 2 });

// --- SLIDE 7: CBOM + REPORTING ---
const s7 = pres.addSlide({ masterName: 'Standard' });
s7.addText('Turn cryptographic findings into portable security evidence', { x: 0.3, y: 0.7, w: 9, h: 0.5, fontSize: 24, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });

const reports = ['CycloneDX 1.6 CBOM', 'SARIF 2.1.0', 'JSON / CSV', 'HTML / PDF / Markdown'];
reports.forEach((r, i) => {
  addCard(s7, 0.3 + (i % 2) * 4.7, 1.3 + Math.floor(i / 2) * 1.5, 4.5, 1.2, 'Export Format', r);
});
s7.addImage({ path: '/sessions/trusting-laughing-lamport/mnt/QuantumShield/tests/results/e2e_07_cbom.png', x: 3, y: 4, w: 4, h: 1.2 });

// --- SLIDE 8: VALIDATION / PROOF ---
const s8 = pres.addSlide({ masterName: 'Standard' });
s8.addText('Built and validated as a real working system', { x: 0.3, y: 0.7, w: 9, h: 0.5, fontSize: 24, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });

const metrics = [
  { v: '71/71', l: 'Automated Tests Passed' },
  { v: '1.000', l: 'Precision (Controlled Corpus)' },
  { v: '0.974', l: 'Recall (Controlled Corpus)' },
  { v: '0 Errors', l: 'CBOM Schema Validation' },
];
metrics.forEach((m, i) => {
  const x = 0.3 + (i * 2.4);
  s8.addShape(pres.ShapeType.roundRect, { x, y: 2, w: 2.2, h: 1.5, fill: { color: COLORS.bg_card }, line: { color: COLORS.accent, width: 1 }, rectRadius: 0.1 });
  s8.addText(m.v, { x, y: 2.2, w: 2.2, h: 0.5, fontSize: 24, color: COLORS.accent, bold: true, align: 'center', isTextBox: true });
  s8.addText(m.l, { x, y: 2.7, w: 2.2, h: 0.6, fontSize: 10, color: COLORS.text_muted, align: 'center', isTextBox: true });
});

s8.addText('External Targets: OpenSSL 3.3.0, CPython 3.12.3, OpenSSH 9.7', { x: 0.3, y: 4.2, w: 9, h: 0.3, fontSize: 14, color: COLORS.text_main, align: 'center', isTextBox: true });

// --- SLIDE 9: WHY QUANTUMSHIELD ---
const s9 = pres.addSlide({ masterName: 'Standard' });
s9.addText('Built for the gap between vulnerability scanning and quantum readiness', { x: 0.3, y: 0.7, w: 9, h: 0.5, fontSize: 24, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });

s9.addShape(pres.ShapeType.rect, { x: 0.3, y: 1.5, w: 4.5, h: 3, fill: { color: COLORS.bg_card }, line: { color: COLORS.text_muted, width: 1 } });
s9.addText('Generic SAST/SCA', { x: 0.3, y: 1.6, w: 4.5, h: 0.4, fontSize: 16, color: COLORS.text_muted, bold: true, align: 'center', isTextBox: true });
s9.addText('Focus: CVEs and Library Versions\nNo Quantum Classification\nNo HNDL/TNFL Modeling\nNo CBOM standards', { x: 0.3, y: 2, w: 4.5, h: 2, fontSize: 12, color: COLORS.text_muted, align: 'left', isTextBox: true });

s9.addShape(pres.ShapeType.rect, { x: 5.2, y: 1.5, w: 4.5, h: 3, fill: { color: COLORS.bg_card }, line: { color: COLORS.accent, width: 2 } });
s9.addText('QuantumShield', { x: 5.2, y: 1.6, w: 4.5, h: 0.4, fontSize: 16, color: COLORS.accent, bold: true, align: 'center', isTextBox: true });
s9.addText('Cryptographic Visibility\nShor/Grover Classification\nHNDL/TNFL Analysis\nMosca Simulation\nDeterministic Risk Scoring\nNIST PQC Recommendations\nCBOM Generation\nOffline-First Analysis', { x: 5.2, y: 2, w: 4.5, h: 2, fontSize: 12, color: COLORS.text_main, align: 'left', isTextBox: true });

// --- SLIDE 10: IMPACT + ROADMAP ---
const s10 = pres.addSlide({ masterName: 'Standard' });
s10.addText('Make post-quantum readiness measurable', { x: 0.3, y: 0.7, w: 9, h: 0.5, fontSize: 24, color: COLORS.text_main, bold: true, align: 'left', isTextBox: true });

const impacts = [
  { t: 'SECURITY', d: 'Know where vulnerable cryptography exists.' },
  { t: 'RISK', d: 'Understand which assets require attention first.' },
  { t: 'MIGRATION', d: 'Create evidence-backed PQC migration priorities.' },
];
impacts.forEach((imp, i) => {
  addCard(s10, 0.3 + i * 3.2, 1.3, 3, 1, imp.t, imp.d, COLORS.accent);
});

s10.addText('Roadmap (Planned):', { x: 0.3, y: 2.7, w: 9, h: 0.3, fontSize: 14, color: COLORS.accent, bold: true, align: 'left', isTextBox: true });
s10.addText('Continuous Monitoring → Migration Tracking → Expanded Language Coverage → Enterprise Integration', { x: 0.3, y: 3.0, w: 9, h: 0.4, fontSize: 12, color: COLORS.text_muted, align: 'left', isTextBox: true });

s10.addText('QuantumShield | Discover. Quantify. Prioritize. Migrate.', { x: 0.3, y: 4.5, w: 9, h: 0.3, fontSize: 14, color: COLORS.text_main, bold: true, align: 'center', isTextBox: true });
s10.addText('https://quantumshield-seven.vercel.app | GitHub: /shaikmohammedyasin-create/QuantumShield', { x: 0.3, y: 4.8, w: 9, h: 0.3, fontSize: 12, color: COLORS.text_muted, align: 'center', isTextBox: true });

pres.writeFile({ fileName: '/sessions/trusting-laughing-lamport/mnt/QuantumShield/submission/BuildSpark_QuantumShield.pptx' });
