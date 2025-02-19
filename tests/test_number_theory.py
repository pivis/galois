"""
A pytest module to test number theoretic functions.
"""
import pytest

import galois

# pylint: disable=line-too-long


def test_totatives_exceptions():
    with pytest.raises(TypeError):
        galois.totatives(20.0)
    with pytest.raises(ValueError):
        galois.totatives(-1)


def test_totatives():
    # https://oeis.org/A000010
    N = list(range(1, 70))
    PHI = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24, 52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44]  # fmt: skip
    for n, phi in zip(N, PHI):
        assert len(galois.totatives(n)) == phi


def test_euler_phi_exceptions():
    with pytest.raises(TypeError):
        galois.euler_phi(20.0)
    with pytest.raises(ValueError):
        galois.euler_phi(-1)


def test_euler_phi_oeis():
    # https://oeis.org/A000010
    N = list(range(1, 70))
    PHI = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24, 52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44]  # fmt: skip
    for n, phi in zip(N, PHI):
        assert galois.euler_phi(n) == phi


def test_euler_phi(euler_phi):
    X, Z = euler_phi["X"], euler_phi["Z"]
    for x, z in zip(X, Z):
        assert galois.euler_phi(x) == z


def test_carmichael_lambda_exceptions():
    with pytest.raises(TypeError):
        galois.carmichael_lambda(20.0)
    with pytest.raises(ValueError):
        galois.carmichael_lambda(-1)


def test_carmichael_lambda_oeis():
    # https://oeis.org/A002322
    N = list(range(1, 82))
    LAMBDA = [1, 1, 2, 2, 4, 2, 6, 2, 6, 4, 10, 2, 12, 6, 4, 4, 16, 6, 18, 4, 6, 10, 22, 2, 20, 12, 18, 6, 28, 4, 30, 8, 10, 16, 12, 6, 36, 18, 12, 4, 40, 6, 42, 10, 12, 22, 46, 4, 42, 20, 16, 12, 52, 18, 20, 6, 18, 28, 58, 4, 60, 30, 6, 16, 12, 10, 66, 16, 22, 12, 70, 6, 72, 36, 20, 18, 30, 12, 78, 4, 54]  # fmt: skip
    for n, lambda_ in zip(N, LAMBDA):
        assert galois.carmichael_lambda(n) == lambda_


def test_carmichael_lambda(carmichael_lambda):
    X, Z = carmichael_lambda["X"], carmichael_lambda["Z"]
    for x, z in zip(X, Z):
        assert galois.carmichael_lambda(x) == z


def test_is_cyclic_exceptions():
    with pytest.raises(TypeError):
        galois.is_cyclic(20.0)
    with pytest.raises(ValueError):
        galois.is_cyclic(-1)


def test_is_cyclic(is_cyclic):
    X, Z = is_cyclic["X"], is_cyclic["Z"]
    for x, z in zip(X, Z):
        assert galois.is_cyclic(x) == z


def test_legendre_symbol_exceptions():
    with pytest.raises(TypeError):
        galois.legendre_symbol(3.0, 7)
    with pytest.raises(TypeError):
        galois.legendre_symbol(3, 7.0)
    with pytest.raises(ValueError):
        galois.legendre_symbol(3, 4)
    with pytest.raises(ValueError):
        galois.legendre_symbol(3, 2)


def test_legendre_symbol():
    # https://oeis.org/A102283
    assert [galois.legendre_symbol(n, 3) for n in range(105)] == [0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1]  # fmt: skip
    # https://oeis.org/A080891
    assert [galois.legendre_symbol(n, 5) for n in range(101)] == [0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0]  # fmt: skip
    # https://oeis.org/A175629
    assert [galois.legendre_symbol(n, 7) for n in range(87)] == [0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1]  # fmt: skip
    # https://oeis.org/A011582
    assert [galois.legendre_symbol(n, 11) for n in range(81)] == [0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1]  # fmt: skip
    # https://oeis.org/A011583
    assert [galois.legendre_symbol(n, 13) for n in range(81)] == [0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1]  # fmt: skip
    # ...
    # https://oeis.org/A165573
    assert [galois.legendre_symbol(n, 257) for n in range(82)] == [0, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1]  # fmt: skip
    # https://oeis.org/A165574
    assert [galois.legendre_symbol(n, 263) for n in range(84)] == [0, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1]  # fmt: skip


def test_jacobi_symbol_exceptions():
    with pytest.raises(TypeError):
        galois.jacobi_symbol(3.0, 7)
    with pytest.raises(TypeError):
        galois.jacobi_symbol(3, 7.0)
    with pytest.raises(ValueError):
        galois.jacobi_symbol(3, 4)
    with pytest.raises(ValueError):
        galois.jacobi_symbol(3, 1)


def test_jacobi_symbol():
    # https://oeis.org/A102283
    assert [galois.jacobi_symbol(n, 3) for n in range(105)] == [0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1]  # fmt: skip
    # https://oeis.org/A080891
    assert [galois.jacobi_symbol(n, 5) for n in range(101)] == [0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0]  # fmt: skip
    # https://oeis.org/A175629
    assert [galois.jacobi_symbol(n, 7) for n in range(87)] == [0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1]  # fmt: skip
    # https://oeis.org/A011582
    assert [galois.jacobi_symbol(n, 11) for n in range(81)] == [0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1]  # fmt: skip
    # https://oeis.org/A011583
    assert [galois.jacobi_symbol(n, 13) for n in range(81)] == [0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1]  # fmt: skip

    # https://oeis.org/A102283
    assert [galois.jacobi_symbol(n, 15) for n in range(76)] == [0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0]  # fmt: skip
    # https://oeis.org/A322829
    assert [galois.jacobi_symbol(n, 21) for n in range(85)] == [0, 1, -1, 0, 1, 1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 1, 1, 0, -1, 1, 0]  # fmt: skip


def test_kronecker_symbol_exceptions():
    with pytest.raises(TypeError):
        galois.kronecker_symbol(3.0, 7)
    with pytest.raises(TypeError):
        galois.kronecker_symbol(3, 7.0)


def test_kronecker_symbol():
    # https://oeis.org/A102283
    assert [galois.kronecker_symbol(n, 3) for n in range(105)] == [0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1]  # fmt: skip
    # https://oeis.org/A080891
    assert [galois.kronecker_symbol(n, 5) for n in range(101)] == [0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0, 1, -1, -1, 1, 0]  # fmt: skip
    # https://oeis.org/A175629
    assert [galois.kronecker_symbol(n, 7) for n in range(87)] == [0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1, -1, 1, -1, -1, 0, 1, 1]  # fmt: skip
    # https://oeis.org/A011582
    assert [galois.kronecker_symbol(n, 11) for n in range(81)] == [0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 0, 1, -1, 1]  # fmt: skip
    # https://oeis.org/A011583
    assert [galois.kronecker_symbol(n, 13) for n in range(81)] == [0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 0, 1, -1]  # fmt: skip

    # https://oeis.org/A102283
    assert [galois.kronecker_symbol(n, 15) for n in range(76)] == [0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0, 1, 1, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, -1, -1, 0]  # fmt: skip
    # https://oeis.org/A322829
    assert [galois.kronecker_symbol(n, 21) for n in range(85)] == [0, 1, -1, 0, 1, 1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 0, -1, 0, -1, -1, 0, -1, 0, 0, 1, 1, 0, -1, 1, 0]  # fmt: skip

    # https://oeis.org/A289741
    assert [galois.kronecker_symbol(-20, n) for n in range(81)] == [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1, 0]  # fmt: skip
    # https://oeis.org/A226162
    assert [galois.kronecker_symbol(-5, n) for n in range(90)] == [0, 1, -1, 1, 1, 0, -1, 1, -1, 1, 0, -1, 1, -1, -1, 0, 1, -1, -1, -1, 0, 1, 1, 1, -1, 0, 1, 1, 1, 1, 0, -1, -1, -1, 1, 0, 1, -1, 1, -1, 0, 1, -1, 1, -1, 0, -1, 1, 1, 1, 0, -1, -1, -1, -1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 1, 0, 1, 1, -1, 1, 0, -1, -1, -1, 1, 0, -1, -1, 1, -1, 0, 1, -1, 1, 1, 0, -1, 1, 1, 1]  # fmt: skip
    # https://oeis.org/A034947
    assert [galois.kronecker_symbol(-1, n) for n in range(1, 82)] == [1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1]  # fmt: skip
    # https://oeis.org/A091337
    assert [galois.kronecker_symbol(2, n) for n in range(1, 106)] == [1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1, 0, -1, 0, -1, 0, 1, 0, 1]  # fmt: skip
    # https://oeis.org/A091338
    assert [galois.kronecker_symbol(3, n) for n in range(1, 103)] == [1, -1, 0, 1, -1, 0, -1, -1, 0, 1, 1, 0, 1, 1, 0, 1, -1, 0, -1, -1, 0, -1, 1, 0, 1, -1, 0, -1, -1, 0, -1, -1, 0, 1, 1, 0, 1, 1, 0, 1, -1, 0, -1, 1, 0, -1, 1, 0, 1, -1, 0, 1, -1, 0, -1, 1, 0, 1, 1, 0, 1, 1, 0, 1, -1, 0, -1, -1, 0, -1, 1, 0, 1, -1, 0, -1, -1, 0, -1, -1, 0, 1, 1, 0, 1, 1, 0, -1, -1, 0, -1, 1, 0, -1, 1, 0, 1, -1, 0, 1, -1, 0]  # fmt: skip
    # https://oeis.org/A322796
    assert [galois.kronecker_symbol(6, n) for n in range(85)] == [0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0, -1, 0]  # fmt: skip
    # https://oeis.org/A089509
    assert [galois.kronecker_symbol(7, n) for n in range(1, 107)] == [1, 1, 1, 1, -1, 1, 0, 1, 1, -1, -1, 1, -1, 0, -1, 1, -1, 1, 1, -1, 0, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, 1, -1, -1, 0, 1, 1, 1, -1, -1, -1, 0, -1, -1, -1, -1, 1, 1, 0, 1, -1, -1, 1, 1, 1, 0, 1, 1, 1, -1, -1, 1, 0, 1, 1, -1, -1, -1, -1, 0, -1, 1, -1, 1, 1, 1, 0, -1, -1, -1, 1, -1, 1, 0, 1, -1, 1, -1, -1, -1, 0, -1, 1, 1, -1, 1, -1, 0, -1, 1, -1, -1, 1, -1, 0, 1]  # fmt: skip
