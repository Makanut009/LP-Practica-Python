// Generated from /home/jordi/Escritorio/FIB/LP/Python/Pràctica/cl/Skyline.g by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SkylineParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, VAR=5, NUM=6, PER=7, MES=8, MENYS=9, NL=10;
	public static final int
		RULE_root = 0, RULE_instruccio = 1, RULE_assig = 2, RULE_expr = 3, RULE_simbol = 4, 
		RULE_edifici = 5;
	public static final String[] ruleNames = {
		"root", "instruccio", "assig", "expr", "simbol", "edifici"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "':='", "'('", "','", "')'", null, null, "'*'", "'+'", "'-'", "'\n'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, "VAR", "NUM", "PER", "MES", "MENYS", "NL"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Skyline.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SkylineParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class RootContext extends ParserRuleContext {
		public InstruccioContext instruccio() {
			return getRuleContext(InstruccioContext.class,0);
		}
		public TerminalNode EOF() { return getToken(SkylineParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			instruccio();
			setState(13);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstruccioContext extends ParserRuleContext {
		public AssigContext assig() {
			return getRuleContext(AssigContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public InstruccioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccio; }
	}

	public final InstruccioContext instruccio() throws RecognitionException {
		InstruccioContext _localctx = new InstruccioContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instruccio);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(15);
				assig();
				}
				break;
			case 2:
				{
				setState(16);
				expr(0);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssigContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(SkylineParser.VAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssigContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assig; }
	}

	public final AssigContext assig() throws RecognitionException {
		AssigContext _localctx = new AssigContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assig);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			match(VAR);
			setState(20);
			match(T__0);
			setState(21);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public EdificiContext edifici() {
			return getRuleContext(EdificiContext.class,0);
		}
		public SimbolContext simbol() {
			return getRuleContext(SimbolContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode PER() { return getToken(SkylineParser.PER, 0); }
		public TerminalNode MES() { return getToken(SkylineParser.MES, 0); }
		public TerminalNode MENYS() { return getToken(SkylineParser.MENYS, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				}
				break;
			case 2:
				{
				setState(24);
				edifici();
				}
				break;
			case 3:
				{
				setState(25);
				simbol();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(39);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(37);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(28);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(29);
						match(PER);
						setState(30);
						expr(5);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(31);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(32);
						match(MES);
						setState(33);
						expr(4);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(34);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(35);
						match(MENYS);
						setState(36);
						expr(3);
						}
						break;
					}
					} 
				}
				setState(41);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class SimbolContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(SkylineParser.VAR, 0); }
		public TerminalNode NUM() { return getToken(SkylineParser.NUM, 0); }
		public SimbolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simbol; }
	}

	public final SimbolContext simbol() throws RecognitionException {
		SimbolContext _localctx = new SimbolContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_simbol);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			_la = _input.LA(1);
			if ( !(_la==VAR || _la==NUM) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EdificiContext extends ParserRuleContext {
		public List<TerminalNode> NUM() { return getTokens(SkylineParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(SkylineParser.NUM, i);
		}
		public EdificiContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_edifici; }
	}

	public final EdificiContext edifici() throws RecognitionException {
		EdificiContext _localctx = new EdificiContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_edifici);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(T__1);
			setState(45);
			match(NUM);
			setState(46);
			match(T__2);
			setState(47);
			match(NUM);
			setState(48);
			match(T__2);
			setState(49);
			match(NUM);
			setState(50);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 3:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f\67\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\3\2\3\2\3\3\3\3\5\3\24\n\3\3"+
		"\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\35\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\7\5(\n\5\f\5\16\5+\13\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\2\3\b\b\2\4\6\b\n\f\2\3\3\2\7\b\2\66\2\16\3\2\2\2\4\23\3\2\2\2\6\25"+
		"\3\2\2\2\b\34\3\2\2\2\n,\3\2\2\2\f.\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2"+
		"\3\20\3\3\2\2\2\21\24\5\6\4\2\22\24\5\b\5\2\23\21\3\2\2\2\23\22\3\2\2"+
		"\2\24\5\3\2\2\2\25\26\7\7\2\2\26\27\7\3\2\2\27\30\5\b\5\2\30\7\3\2\2\2"+
		"\31\35\b\5\1\2\32\35\5\f\7\2\33\35\5\n\6\2\34\31\3\2\2\2\34\32\3\2\2\2"+
		"\34\33\3\2\2\2\35)\3\2\2\2\36\37\f\6\2\2\37 \7\t\2\2 (\5\b\5\7!\"\f\5"+
		"\2\2\"#\7\n\2\2#(\5\b\5\6$%\f\4\2\2%&\7\13\2\2&(\5\b\5\5\'\36\3\2\2\2"+
		"\'!\3\2\2\2\'$\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\t\3\2\2\2+)\3\2"+
		"\2\2,-\t\2\2\2-\13\3\2\2\2./\7\4\2\2/\60\7\b\2\2\60\61\7\5\2\2\61\62\7"+
		"\b\2\2\62\63\7\5\2\2\63\64\7\b\2\2\64\65\7\6\2\2\65\r\3\2\2\2\6\23\34"+
		"\')";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}